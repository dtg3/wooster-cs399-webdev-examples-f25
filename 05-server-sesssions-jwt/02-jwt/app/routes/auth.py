from flask import Blueprint, jsonify, request, current_app
from argon2 import PasswordHasher
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies
)

ph = PasswordHasher()

# Create a Blueprint for authentication-related routes
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    # Get the username and password from the JSON payload
    data = request.get_json()
    username, password = data["username"], data["password"]

    # Check if the user already is stored in our "database"
    if username in current_app.USERS:
        return jsonify(msg="User already exists"), 400

    # We will store a salted hash of the password value
    current_app.USERS[username] = {"password": ph.hash(password)}
    return jsonify(msg="User registered"), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Handles user login.
    If credentials are valid, it creates an access and a refresh token and sets them in cookies.
    """
    # Get the login credentials
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # In a real app, you would verify against a database
    try:
        # If the username is not in our database, we have invalid credentials
        if not username in current_app.USERS:
            raise Exception
        # If we found the user, lets make sure the password matches our hash
        ph.verify(current_app.USERS[username]["password"], password)
    except Exception:
        return jsonify(msg="Bad credentials"), 401

    # Create the JWT tokens
    #   Since we enabled the CSRF protection we will get an:
    #   * access and CSRF token
    #   * a refresh token to generate new acces and CSRF tokens
    #   These tokens will be in the JWT payload and be HTTPOnly.
    #
    #   We will also get a CSRF token cookie that is non-HTTPOnly
    #   so our client scripts can read it. This will be sent in headers
    #   to validate our requests came from us.
    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)

    # Create the response and set the JWT cookies
    response = jsonify({"msg": "Login successful"})

    # Set the JWT payload to be sent back with the response
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)
    return response


@auth_bp.route("/logout", methods=["POST"])
def logout():
    # Unsets both access and refresh JWT cookies.
    response = jsonify({"msg": "Logout successful"})
    unset_jwt_cookies(response)
    return response


@auth_bp.route("/protected", methods=["GET"])
@jwt_required() # This decorator means you need a valid JWT access token
def protected():
    # Access the identity of the current user with get_jwt_identity
    #   The CSRF token is automatically checked.
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True) # Enabling refresh generates a new access token
def refresh():
    
    # Requires a valid refresh token to create a new access token
    #   The CSRF token is automatically checked.
    #   NOTE: This does not do token rotation as that would also require
    #   generating a new refresh token too.
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)

    # The access cookie needs to be reset
    response = jsonify({"msg": "Access token refreshed"})
    set_access_cookies(response, new_access_token)

    return response
