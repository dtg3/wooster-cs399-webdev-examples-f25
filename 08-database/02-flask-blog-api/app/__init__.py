import os
from dotenv import load_dotenv
from flask import Flask
from .routes.authors import bp as authors_bp
from .routes.posts import bp as posts_bp
from .models.database import init_db, close_db

# Load environment variables from .flaskenv
load_dotenv()

def create_app():
    # Create and configure the app
    app = Flask(__name__)
    
    # Default Configuration (e.g., using a secret key for sessions/security)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        DATABASE=os.environ.get('DATABASE'), # Models uses this name directly
    )

    # Register the function to close the database connection after each request
    app.teardown_appcontext(close_db)

    # Register the 'authors' API blueprint
    app.register_blueprint(authors_bp, url_prefix='/api/v1/authors')
    
    # Register the 'posts' API blueprint
    app.register_blueprint(posts_bp, url_prefix='/api/v1/posts')

    @app.cli.command("initdb")
    def init_database():
        init_db()

    return app
