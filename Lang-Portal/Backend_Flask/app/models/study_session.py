from app import db
from datetime import datetime

class StudySession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    activity_type = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    group = db.relationship('Group', back_populates='study_sessions')
    word_reviews = db.relationship('WordReview', back_populates='study_session')

    def get_accuracy(self):
        if not self.word_reviews:
            return 0
        correct = sum(1 for review in self.word_reviews if review.is_correct)
        return (correct / len(self.word_reviews)) * 100

    def __repr__(self):
        return f'<StudySession {self.id}>' 