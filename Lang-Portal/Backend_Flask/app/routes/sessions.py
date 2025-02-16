from flask import Blueprint, request, jsonify
from app.models.study_session import StudySession
from app.models.word_review import WordReview
from app.schemas import StudySessionSchema, WordReviewSchema
from app import db
from app.utils import paginate_results, handle_errors
from datetime import datetime

sessions_bp = Blueprint('sessions', __name__)
session_schema = StudySessionSchema()
sessions_schema = StudySessionSchema(many=True)
review_schema = WordReviewSchema()

@sessions_bp.route('', methods=['GET'])
@handle_errors
def get_sessions():
    query = StudySession.query.order_by(StudySession.created_at.desc())
    return jsonify(paginate_results(query, sessions_schema))

@sessions_bp.route('', methods=['POST'])
@handle_errors
def create_session():
    data = request.get_json()
    
    new_session = StudySession(
        group_id=data['group_id'],
        activity_type=data['activity_type']
    )
    
    db.session.add(new_session)
    db.session.commit()
    
    return jsonify(session_schema.dump(new_session)), 201

@sessions_bp.route('/<int:session_id>/reviews', methods=['POST'])
@handle_errors
def create_review(session_id):
    data = request.get_json()
    
    review = WordReview(
        word_id=data['word_id'],
        study_session_id=session_id,
        is_correct=data['is_correct']
    )
    
    db.session.add(review)
    db.session.commit()
    
    return jsonify(review_schema.dump(review)), 201 