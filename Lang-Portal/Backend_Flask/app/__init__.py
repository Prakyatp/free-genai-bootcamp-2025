from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app(config_class=None):
    app = Flask(__name__)
    
    if config_class is None:
        app.config.from_object('config.Config')
    else:
        app.config.from_object(config_class)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Import blueprints
    from app.routes.words import words_bp
    from app.routes.groups import groups_bp
    from app.routes.sessions import sessions_bp
    from app.routes.dashboard import dashboard_bp

    # Register blueprints with /api prefix
    app.register_blueprint(words_bp, url_prefix='/api')
    app.register_blueprint(groups_bp, url_prefix='/api')
    app.register_blueprint(sessions_bp, url_prefix='/api')
    app.register_blueprint(dashboard_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to the Language Learning API",
            "endpoints": {
                "words": "/api/words",
                "groups": "/api/groups",
                "sessions": "/api/sessions",
                "dashboard": "/api/dashboard/stats"
            }
        })

    return app