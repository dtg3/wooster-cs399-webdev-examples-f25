from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

from ..models import database as db

posts_bp = Blueprint('post_routes', __name__, url_prefix='/api/v1')

@posts_bp.route('/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    
    if not title or len(title.strip()) == 0:
        return jsonify({'error': 'Title is required'}), 400
    
    if not content or len(content.strip()) == 0:
        return jsonify({'error': 'Content is required'}), 400
    
    try:
        new_post = db.create_post(title, content)
        return jsonify(new_post.to_dict()), 201 # 201 Created
        
    except IntegrityError as e:
        return jsonify({'error': f"Database error creating post: {e}"}), 500

@posts_bp.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    rows_deleted = db.delete_post(post_id)

    if rows_deleted == 0:
        return jsonify({'success': False, 'message': f"Post ID {post_id} not found."}), 404
    
    return jsonify({'success': True, 'message': f'Post ID {post_id} deleted'}), 200

@posts_bp.route('/posts/<int:post_id>', methods=['PATCH'])
def edit_post(post_id):
    data = request.get_json()
    new_title = data.get('title')
    new_content = data.get('content')
    
    if new_title and len(new_title.strip()) == 0:
        return jsonify({'error': 'Title field cannot be empty'}), 400
    
    if new_content and len(new_content.strip()) == 0:
        return jsonify({'error': 'Content field cannot be empty'}), 400
    
    rows_updated = db.update_post(post_id, new_title, new_content)

    if rows_updated == 0:
        if db.get_post_by_id(post_id) is None:
            return jsonify({'success': False, 'message': f"Post ID {post_id} not found."}), 404
        else:
            return jsonify({'message': 'Post found but no changes applied'}), 200

    updated_post = db.get_post_by_id(post_id)
    
    return jsonify(updated_post.to_dict()), 200 # 200 OK


@posts_bp.route('/posts', methods=['GET'])
@posts_bp.route('/posts/<int:post_id>', methods=['GET'])
def get_posts(post_id=None):
    posts = []
    if not post_id:
        posts = db.get_all_posts()
    else:
        posts = db.get_post_by_id(post_id)
    
    posts_list = [p.to_dict() for p in posts]
    return jsonify(posts_list)