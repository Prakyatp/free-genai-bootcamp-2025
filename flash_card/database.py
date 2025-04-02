from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    progress = relationship('UserProgress', back_populates='user')

class Word(Base):
    __tablename__ = 'words'
    
    word_id = Column(Integer, primary_key=True)
    kannada_word = Column(String(100), nullable=False)
    english_meaning = Column(String(100), nullable=False)
    image_url = Column(String(255))
    
    progress = relationship('UserProgress', back_populates='word')

class UserProgress(Base):
    __tablename__ = 'user_progress'
    
    progress_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    word_id = Column(Integer, ForeignKey('words.word_id'))
    is_known = Column(Boolean, default=False)
    last_attempted = Column(DateTime, default=datetime.utcnow)
    
    user = relationship('User', back_populates='progress')
    word = relationship('Word', back_populates='progress') 