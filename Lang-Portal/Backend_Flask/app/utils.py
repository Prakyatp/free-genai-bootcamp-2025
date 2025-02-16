from flask import request, jsonify
from functools import wraps

def paginate_results(query, schema):
    """Utility function for pagination"""
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    offset = (page - 1) * limit

    total = query.count()
    items = query.offset(offset).limit(limit).all()
    
    return {
        'items': schema.dump(items),
        'total': total,
        'page': page,
        'pages': (total + limit - 1) // limit
    }

def handle_errors(f):
    """Error handling decorator"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return wrapper 