from app import db
from datetime import datetime

class WordReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('word.word_id'), nullable=False)
    study_session_id = db.Column(db.Integer, db.ForeignKey('study_session.id'), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    word = db.relationship('Word', back_populates='reviews')
    study_session = db.relationship('StudySession', back_populates='word_reviews')

    def __repr__(self):
        return f'<WordReview {self.id}>' 