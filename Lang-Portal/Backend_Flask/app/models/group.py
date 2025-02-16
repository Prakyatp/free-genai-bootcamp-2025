from app import db
from datetime import datetime

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    words = db.relationship('Word', secondary='words_groups', back_populates='groups')
    study_sessions = db.relationship('StudySession', back_populates='group')

    def __repr__(self):
        return f'<Group {self.name}>' 