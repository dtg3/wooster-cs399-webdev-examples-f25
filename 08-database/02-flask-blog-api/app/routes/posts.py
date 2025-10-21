from flask import Blueprint, request, jsonify
from ..models.database import add_post, get_all_posts, get_post_by_id, delete_post_by_id
import sqlite3

# Create the Blueprint instance
bp = Blueprint('posts', __name__)

@bp.route('/', methods=['GET', 'POST'])
def handle_posts():

    if request.method == 'POST':
        data = request.get_json()
        required_fields = ['title', 'author_id']
        
        if not data or any(field not in data for field in required_fields):
            return jsonify({'error': f'Missing required fields: {", ".join(required_fields)}'}), 400 # Bad Request

        title = data['title']
        content = data.get('content', '')
        author_id = data['author_id']

        try:
            post_id = add_post(title, content, author_id)
            
            # Fetch the newly created post for the response
            new_post = get_post_by_id(post_id) 
            return jsonify(new_post), 201
        except sqlite3.IntegrityError:
            # Handles FOREIGN KEY constraint violation (author_id does not exist)
            return jsonify({'error': f'Author with ID {author_id} does not exist.'}), 400 # Bad Request
        except Exception as e:
            return jsonify({'error': f'Database error: {str(e)}'}), 500 # Internal Server Error

    posts = get_all_posts()
    return jsonify(posts), 200

@bp.route('/<int:post_id>', methods=['GET', 'DELETE'])
def handle_single_post(post_id):

    post = get_post_by_id(post_id)

    if not post:
        return jsonify({'error': f'Post with ID {post_id} not found'}), 404 # Not Found

    if request.method == 'DELETE':
        rows_deleted = delete_post_by_id(post_id)
        if rows_deleted > 0:
            return jsonify({'message': f'Post with ID {post_id} deleted successfully'}), 200
        else:
            return jsonify({'error': f'Failed to delete post with ID {post_id}'}), 500 # Internal Server Error

    return jsonify(post), 200
