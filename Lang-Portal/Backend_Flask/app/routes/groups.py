from flask import Blueprint, request, jsonify
from app.models.group import Group
from app.schemas import GroupSchema
from app import db

groups_bp = Blueprint('groups', __name__)
group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)

@groups_bp.route('/groups', methods=['GET'])
def get_groups():
    groups = Group.query.all()
    return jsonify({
        'items': groups_schema.dump(groups),
        'total': len(groups)
    })