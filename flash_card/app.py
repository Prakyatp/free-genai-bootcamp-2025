from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
import logging
import time

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///flashcards.db')
DBSession = sessionmaker(bind=engine)

class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    english_word = Column(String(50), nullable=False)
    kannada_word = Column(String(50), nullable=False)

Base.metadata.create_all(engine)

def generate_initial_words():
    """Generate 50 word pairs and store them in the database"""
    db = DBSession()
    
    # Check if database is empty
    if db.query(Word).first() is not None:
        logger.info("Database already contains words")
        db.close()
        return

    logger.info("Generating initial 50 words...")
    
    try:
        # Get 50 English words
        prompt = """Generate 50 simple English nouns (like: cat, dog, house, tree, book).
                   Return only the words separated by commas, no explanations."""
        
        response = requests.post('http://localhost:11434/api/generate',
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )
        
        if response.status_code != 200:
            logger.error("Failed to get English words")
            return
            
        english_words = [word.strip().lower() for word in response.json()['response'].split(',')]
        logger.info(f"Generated {len(english_words)} English words")

        # Get Kannada translations
        for english_word in english_words:
            translate_prompt = f"Translate this English word to Kannada: {english_word}. Reply with just the Kannada word."
            
            translate_response = requests.post('http://localhost:11434/api/generate',
                json={
                    "model": "mistral",
                    "prompt": translate_prompt,
                    "stream": False
                }
            )
            
            if translate_response.status_code == 200:
                kannada_word = translate_response.json()['response'].strip()
                
                # Store in database
                new_word = Word(english_word=english_word, kannada_word=kannada_word)
                db.add(new_word)
                logger.info(f"Added word pair: {english_word} - {kannada_word}")
                
                # Small delay to prevent overwhelming Ollama
                time.sleep(0.5)
        
        db.commit()
        logger.info("Successfully generated and stored initial words")
        
    except Exception as e:
        logger.error(f"Error generating initial words: {str(e)}")
        db.rollback()
    finally:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word', methods=['GET'])
def get_word():
    db = DBSession()
    try:
        # Get random word from database
        word = db.query(Word).order_by(func.random()).first()
        
        if not word:
            return jsonify({'error': 'No words available in database'})
        
        return jsonify({
            'english_word': word.english_word,
            'kannada_word': word.kannada_word
        })
        
    except Exception as e:
        logger.error(f"Error getting word: {str(e)}")
        return jsonify({'error': 'Failed to get word'})
    finally:
        db.close()

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    user_answer = data.get('answer', '').strip()
    correct_answer = data.get('correct_answer', '').strip()
    
    is_correct = user_answer.lower() == correct_answer.lower()
    
    return jsonify({
        'correct': is_correct,
        'correct_answer': correct_answer
    })

if __name__ == '__main__':
    # Generate initial words if database is empty
    generate_initial_words()
    app.run(debug=True) 