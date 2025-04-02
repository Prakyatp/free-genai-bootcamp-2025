import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    SQLITE_DB_PATH = 'sqlite:///flashcard.db'
    STABILITY_API_KEY = os.getenv('STABILITY_API_KEY')
    STABILITY_HOST = os.getenv('STABILITY_HOST', 'grpc.stability.ai:443') 