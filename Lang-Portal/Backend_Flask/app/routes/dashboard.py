from flask import Blueprint, jsonify
from app.models.study_session import StudySession
from app.models.word_review import WordReview
from app import db

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard/stats', methods=['GET'])
def get_stats():
    return jsonify({
        'total_words_learned': 0,
        'accuracy_rate': 0,
        'recent_sessions': [],
        'activity_breakdown': []
    })