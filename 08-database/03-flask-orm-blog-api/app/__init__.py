import os
from flask import Flask
from dotenv import load_dotenv

from models.database import db
from routes.authors import authors_bp
from routes.posts import posts_bp

# Load environment variables from .flaskenv
load_dotenv()

def create_app():
    # Create and configure the app
    app = Flask(__name__)
    
    # Default Configuration (e.g., using a secret key for sessions/security)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        # Configure SQLite DB path in the instance folder
        SQLALCHEMY_DATABASE_URI=f'sqlite:///{os.path.join(app.instance_path, os.environ.get('DATABASE'))}',

        # This is a feature from Flask-SQLAlchemy that emits signals when SQLAlchemy objects are changed
        #   this could be useful if we need to track when posts or authors are updated, but there is a
        #   performance hit to doing so. We don't really need it, so we turn it off.
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # Connect Flask-SQLAlchemy with our app
    db.init_app(app)

    # Register the 'authors' API blueprint
    app.register_blueprint(authors_bp, url_prefix='/api/v1/authors')

    # Register the 'posts' API blueprint
    app.register_blueprint(posts_bp, url_prefix='/api/v1/posts')

    @app.cli.command("initdb")
    def init_database():
        db.create_all() # SQLAlchemy to create all the tables

    return app
