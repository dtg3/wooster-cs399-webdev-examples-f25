import os
import datetime
from flask import Flask
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)

    # Fake "database"
    app.USERS = {}

    # IMPORTANT: In a production environment, use a long, random, and secure secret key.
    app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY')

    # Configure token lifetimes.
    #   We are using short spans here to see the effects of expiration.
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(seconds=15)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(seconds=45)

    # Common defaults, but shorter is more secure
    # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=15)
    # app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(days=30)
    
    # JWT can be sent in a variety of methods
    #   ["headers", "cookies", "json", "query_string"]
    #   I'm going to only use cookies for now.
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    
    # Configure the JWT support CSRF protection.
    app.config["JWT_COOKIE_CSRF_PROTECT"] = True

    # My cookies will all come from the same site, so strict is fine
    app.config["JWT_COOKIE_SAMESITE"] = 'Strict'

    # JWT cookies will be HTTPOnly to prevent scripts from reading them
    app.config["JWT_COOKIE_HTTPONLY"] = True

    # For local HTTP dev only, you may temporarily set:
    app.config["JWT_COOKIE_SECURE"] = False

    # Alternative Settings for Production
    # app.config["JWT_COOKIE_SECURE"] = True        # requires HTTPS
    # app.config["JWT_COOKIE_SAMESITE"] = "Strict"  # Can also use Lax depending on your needs

    # Initialize the Flask-JWT-Extended extension
    jwt = JWTManager(app)

    # Register the blueprint containing the authentication routes
    # Note: The actual routes are now imported from a separate file.
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
