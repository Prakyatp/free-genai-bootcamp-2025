from flask import Blueprint, request, jsonify
from app.models.word import Word
from app.schemas import WordSchema
from app import db

words_bp = Blueprint('words', __name__)
word_schema = WordSchema()
words_schema = WordSchema(many=True)

@words_bp.route('/words', methods=['GET'])
def get_words():
    words = Word.query.all()
    return jsonify({
        'items': words_schema.dump(words),
        'total': len(words)
    })

@words_bp.route('/words/<int:word_id>', methods=['GET'])
def get_word(word_id):
    word = Word.query.get_or_404(word_id)
    return jsonify(word_schema.dump(word))