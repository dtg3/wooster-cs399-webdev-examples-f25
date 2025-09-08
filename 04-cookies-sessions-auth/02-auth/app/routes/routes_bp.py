from flask import Blueprint, jsonify, request, session, current_app
from argon2 import PasswordHasher

ph = PasswordHasher()

# Create a Blueprint instance
routes_bp = Blueprint('routes_bp', __name__)


@routes_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    current_app.users[username] = ph.hash(password)

    return jsonify(msg="User registered"), 201


@routes_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Basic input validation
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    # Authenticate the user against the mock database.
    if ph.verify(current_app.users.get(username), password):
        # Authentication successful.
        # Store the user's identifier in the Flask session object.
        # Flask handles the secure storage of this session data in a cookie.
        session['user_id'] = username
        return jsonify({"message": f"Login successful, welcome {username}"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


@routes_bp.route('/secret')
def secret():
    # Access the session object to check for an authenticated user.
    user_id = session.get('user_id')

    if user_id:
        # The user_id exists in the session, so the user is logged in.
        return jsonify({
            "message": "This is a protected page. You are authenticated.",
            "user": user_id
        }), 200
    else:
        return jsonify({"message": "Unauthorized access. Please log in."}), 401


@routes_bp.route('/logout', methods=['POST'])
def logout():
    # Use session.pop() to remove the 'user_id' key from the session.
    #   The second argument (None) is a default value to prevent a KeyError if the key doesn't exist.
    #   This only removes the user_id value from the client-side cookie.
    session.pop('user_id', None) 
    return jsonify({"message": "Logout successful"}), 200
