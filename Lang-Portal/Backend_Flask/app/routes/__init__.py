from app.routes.words import words_bp
from app.routes.groups import groups_bp
from app.routes.sessions import sessions_bp
from app.routes.dashboard import dashboard_bp
from app.routes.test import test_bp  # Add this line

__all__ = ['words_bp', 'groups_bp', 'sessions_bp', 'dashboard_bp', 'test_bp']  # Add test_bp here