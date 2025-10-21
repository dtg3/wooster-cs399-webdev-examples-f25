from flask import Blueprint, request, jsonify
from models import db, Post, Author

posts_bp = Blueprint('posts', __name__)

def handle_database_error(e, message="A database error occurred."):
    """Logs the error and returns a 500 JSON response."""
    print(f"Database Error: {e}")
    return jsonify({'error': message}), 500


@posts_bp.route('/', methods=['GET', 'POST'])
def handle_posts():
    if request.method == 'GET':
        try:
            posts = Post.query.all()
            return jsonify([post.to_dict() for post in posts]), 200
        except Exception as e:
            return handle_database_error(e)

    elif request.method == 'POST':
        try:
            data = request.get_json()
            required_fields = ['title', 'author_id']
            if not all(field in data for field in required_fields):
                return jsonify({'error': 'Missing required fields: title, author_id.'}), 400

            author_id = data['author_id']
            author = db.session.get(Author, author_id)
            if not author:
                return jsonify({'error': f"Author with ID {author_id} not found."}), 404

            new_post = Post(
                title=data['title'],
                content=data.get('content'),
                author_id=author_id
            )

            # You can think of the session as a transaction record. When use add() to 
            #   create new records in our database. When we're done, we can call commit()
            #   to finialize the changes.
            # 
            #   It is useful to remember that if you need to add a lot
            #   of data you may not want to call commit() after each individual
            #   add, it will be MUCH slower than writing the transactions in one
            #   "batch" of data.
            db.session.add(new_post)
            db.session.commit()

            return jsonify(new_post.to_dict()), 201
        
        except Exception as e:
            # This is the "bad stuff happened" code.
            #   If for some reason while we were in the middle of getting our transactions
            #   ready to store in the database, something went wrong, we don't want only
            #   some of the data to get updated. Thus, for safety and to ensure data integrity,
            #   we rollback the changes.
            db.session.rollback()
            return handle_database_error(e, "Failed to create post due to internal error.")


@posts_bp.route('/<int:post_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_post_by_id(post_id):
    
    post = db.get_or_404(Post, post_id, description=f"Post with ID {post_id} not found.")

    if request.method == 'GET':
        return jsonify(post.to_dict()), 200

    elif request.method == 'PUT':
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No data provided for update.'}), 400

            if 'title' in data:
                post.title = data['title']
            if 'content' in data:
                post.content = data['content']
            if 'author_id' in data:
                # Ensure new author exists before assigning; throws 404 if not
                author_id = data['author_id']
                author = db.session.get(Author, author_id)
                if not author:
                    return jsonify({'error': f"Cannot update: Author with ID {author_id} not found."}), 404
        
                post.author_id = author_id

            # Changing the existing data doesn't need an add, just a commit to save the
            #   changes to the Model object.
            db.session.commit()
            return jsonify(post.to_dict()), 200
        
        except Exception as e:
            db.session.rollback()
            return handle_database_error(e, "Failed to update post.")

    elif request.method == 'DELETE':
        try:
            db.session.delete(post)
            db.session.commit()
            return jsonify({'message': f'Post with ID {post_id} deleted successfully.'}), 200
        except Exception as e:
            db.session.rollback()
            return handle_database_error(e, f'Failed to delete post with ID {post_id} due to internal error.')