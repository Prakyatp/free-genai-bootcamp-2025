from app import db
from datetime import datetime

words_groups = db.Table('words_groups',
    db.Column('word_id', db.Integer, db.ForeignKey('word.word_id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'), primary_key=True)
)

class Word(db.Model):
    word_id = db.Column(db.Integer, primary_key=True)
    kannada_word = db.Column(db.String(255), nullable=False)
    english_word = db.Column(db.String(255), nullable=False)
    parts = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    groups = db.relationship('Group', secondary=words_groups, back_populates='words')
    reviews = db.relationship('WordReview', back_populates='word')

    def __repr__(self):
        return f'<Word {self.kannada_word}>' 