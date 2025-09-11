from flask import Blueprint, jsonify, request, current_app
from flask_login import login_user, login_required, logout_user, current_user

# This will be our secure password hasher and validator
from argon2 import PasswordHasher

# UUIDs will be used as unique IDs for registered users
import uuid

# We need this user object to help with the login process
from app import User

# This is argon2's password hashing object. We'll just
#   use it to make salted hashes and to verify a plaintext
#   password against a hash.
ph = PasswordHasher()

routes_bp = Blueprint('routes_bp', __name__)


@routes_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    id = str(uuid.uuid4()) # Convert UUID to string for consistency
    current_app.users[id] = { "username" : username, 
                              "password" :  ph.hash(password), # Hash that password!
                              "profile_message" : "Hello, World!"}
    return jsonify(msg="User registered"), 201


@routes_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # A simple way to authenticate against our in-memory data store.
    for user_id, user_data in current_app.users.items():
        print(user_id, user_data)
        # Find the user, and then validate their password. While this seems okay, we actaully
        #   would need to make some changes here to prevent a timing attack if this were
        #   "production" code.
        if user_data["username"] == username and ph.verify(user_data["password"], password):
            print("FOUND ONE!")
            user_obj = User(id=user_id)
            # The login_user() function from Flask-Login manages the session.
            #   It puts the user's ID into Flask's session object, which is now
            #   being saved to the filesystem by Flask-Session.
            login_user(user_obj)
            return jsonify({"message": "Login successful!"})

    return jsonify({"message": "Invalid credentials."}), 401


@routes_bp.route("/profile", methods=["GET"])
@login_required # This decorator protects the route.
def get_profile():

    # Flask-Login provides the `current_user` proxy, which represents the logged-in user.
    #   This object is populated by our `load_user` function after Flask-Session retrieves
    #   the user ID from the server-side session.
    user_data = current_app.users.get(current_user.id)
    if not user_data:
        return jsonify({"message": "User data not found."}), 404
    return jsonify({
        "message": "Welcome to your profile!",
        "user_id": current_user.id,
        "username": user_data["username"],
        "profile_message": user_data["profile_message"],
    })


@routes_bp.route("/profile", methods=["PUT"])
@login_required # Gotta be logged in to access this route. This is protected by Flask-Login
def update_profile():
    data = request.get_json()
    new_message = data.get("profile_message")
    if not new_message:
        return jsonify({"message": "profile_message is required."}), 400
    
    # This line simulates updating a record in a database. The user's ID is safely
    #   retrieved from `current_user` provided by Flask-Login.
    current_app.users[current_user.id]["profile_message"] = new_message
    return jsonify({"message": "Profile message updated successfully!"})


@routes_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    # The logout_user() function clears the session. Flask-Session then removes
    #   the corresponding session
    logout_user()
    return jsonify({"message": "You have been logged out."})


@routes_bp.route("/public", methods=["GET"])
def public():
    return jsonify({"message": "This is a public endpoint."})
