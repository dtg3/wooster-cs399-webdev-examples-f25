from flask import Blueprint, request, jsonify
from ..models.database import add_author, get_all_authors, get_author_by_id, delete_author_by_id
import sqlite3

bp = Blueprint('authors', __name__)

@bp.route('/', methods=['GET', 'POST'])
def handle_authors():

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Missing required parameters: name and email'}), 400 # Bad Request

        name = data['name']
        email = data['email']

        try:
            author_id = add_author(name, email)
            return jsonify({
                'id': author_id,
                'name': name,
                'email': email,
                'message': 'Author created successfully'
            }), 201
        except sqlite3.IntegrityError:
            # Handles UNIQUE constraint violation (e.g., email already exists)
            return jsonify({'error': f'Author with email "{email}" already exists.'}), 409 # Conflict
        except Exception as e:
            return jsonify({'error': f'Database error: {str(e)}'}), 500 # Internal Server Error

    authors = get_all_authors()
    return jsonify(authors), 200

@bp.route('/<int:author_id>', methods=['GET', 'DELETE'])
def handle_single_author(author_id):

    author = get_author_by_id(author_id)

    if not author:
        return jsonify({'error': f'Author with ID {author_id} not found'}), 404 # Not Found

    if request.method == 'DELETE':
        rows_deleted = delete_author_by_id(author_id)
        if rows_deleted > 0:
            return jsonify({'message': f'Author with ID {author_id} deleted successfully. All associated posts were also removed.'}), 200
        else:
            return jsonify({'error': f'Failed to delete author with ID {author_id}'}), 500 # Internal Server Error

    return jsonify(author), 200
