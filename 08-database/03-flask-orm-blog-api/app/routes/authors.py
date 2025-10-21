from flask import Blueprint, request, jsonify
from models import db, Author

authors_bp = Blueprint('authors', __name__)

def handle_database_error(e, message="A database error occurred."):
    """Logs the error and returns a 500 JSON response."""
    print(f"Database Error: {e}")
    return jsonify({'error': message}), 500


@authors_bp.route('/', methods=['GET', 'POST'])
def handle_authors():
    if request.method == 'GET':
        try:
            authors = Author.query.all()
            return jsonify([author.to_dict() for author in authors]), 200
        
        except Exception as e:
            return handle_database_error(e)

    elif request.method == 'POST':
        try:
            data = request.get_json()
            if not data or not data.get('name') or not data.get('email'):
                return jsonify({'error': 'Missing name or email fields.'}), 400

            # Check for unique email
            #
            # Let's break this one down.
            # Author.query => SELECT * FROM authors
            # .filter_by(email=data['email']) => WHERE email = data['email']
            # .first() => LIMIT 1
            #
            # The last part is what executes the query. Common methods are:
            #   * first() => The data may or may not be there, I just need to know (None if not present)
            #   * all() => I want all the results from the query
            #   * one() => There better be one result and ONLY one result (error otherwise).
            if Author.query.filter_by(email=data['email']).first():
                return jsonify({'error': f'Author with email {data["email"]} already exists.'}), 409

            new_author = Author(name=data['name'], email=data['email'])

            # New records need to be added.
            db.session.add(new_author)
            db.session.commit()

            return jsonify(new_author.to_dict()), 201
        
        except Exception as e:
            db.session.rollback()
            return handle_database_error(e, "Failed to create author due to internal error.")

@authors_bp.route('/<int:author_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_author_by_id(author_id):
    
    author = db.session.get(Author, author_id)
    if not author:
        return jsonify({'error': f"Author with ID {author_id} not found."}), 404

    if request.method == 'GET':
        return jsonify(author.to_dict()), 200

    elif request.method == 'PUT':
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No data provided for update.'}), 400

            if 'name' in data:
                author.name = data['name']
            if 'email' in data:
                # Check for uniqueness only if email is changed
                if data['email'] != author.email and Author.query.filter_by(email=data['email']).first():
                    return jsonify({'error': f'Email {data["email"]} is already in use.'}), 409
                author.email = data['email']
            
            db.session.commit()
            return jsonify(author.to_dict()), 200
        
        except Exception as e:
            db.session.rollback()
            return handle_database_error(e, "Failed to update author.")

    elif request.method == 'DELETE':
        try:
            db.session.delete(author)
            db.session.commit()
            return jsonify({'message': f'Author with ID {author_id} and all associated posts deleted successfully.'}), 200
        
        except Exception as e:
            db.session.rollback()
            return handle_database_error(e, f'Failed to delete author with ID {author_id} due to internal error.')