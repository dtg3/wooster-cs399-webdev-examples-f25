from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from ..models import database as db

posts_bp = Blueprint('post_routes', __name__, url_prefix='/api/v1')

@posts_bp.route('/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    try:
        new_post = db.create_post(title, content)
        return jsonify(new_post.to_dict()), 201
    except IntegrityError as e:
        return jsonify({'error': f"Database Error: {e}"}), 500

@posts_bp.route('/posts', methods=["GET"])
def get_posts():
    posts = db.get_all_posts()
    posts_list = [p.to_dict() for p in posts]
    return jsonify(posts_list)