import click
from flask.cli import with_appcontext
from app import db
from app.models.word import Word
from app.models.group import Group
import json

@click.command('seed')
@with_appcontext
def seed_command():
    """Seed the database with initial data"""
    try:
        with open('seeds/initial_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Create groups
        for group_data in data['groups']:
            group = Group(name=group_data['name'])
            db.session.add(group)
        db.session.commit()
        
        # Create words
        for word_data in data['words']:
            word = Word(
                kannada_word=word_data['kannada_word'],
                english_word=word_data['english_word'],
                parts=word_data.get('parts', {})
            )
            
            # Add to groups
            for group_name in word_data.get('groups', []):
                group = Group.query.filter_by(name=group_name).first()
                if group:
                    word.groups.append(group)
            
            db.session.add(word)
        db.session.commit()
        print("Database seeded successfully!")
        
    except Exception as e:
        print(f"Error seeding database: {str(e)}") 