from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Enable CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:8080"],
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    db.init_app(app)

    # Register all blueprints
    from app.routes import words_bp, groups_bp, sessions_bp, dashboard_bp, test_bp
    
    app.register_blueprint(words_bp)
    app.register_blueprint(groups_bp)
    app.register_blueprint(sessions_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(test_bp)

    return app