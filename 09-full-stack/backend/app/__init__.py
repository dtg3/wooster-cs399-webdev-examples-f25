import os
from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy object globally, but without the app
db = SQLAlchemy()

from .routes.posts_api import posts_bp
from .routes.time_api import time_bp

# Load environment variables from .flaskenv
load_dotenv()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    if os.environ.get('FLASK_ENV') == 'development':
        CORS(app)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, os.environ.get('DATABASE', 'blog.db')),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    
    # Register the API blueprints
    app.register_blueprint(posts_bp)
    app.register_blueprint(time_bp)

    # Define where our REACT front end is located for deployment
    REACT_BUILD_DIR = os.path.join(app.root_path, 'static', 'dist')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_react_app(path):
        file_path = os.path.join(REACT_BUILD_DIR, path)
        
        # Check if the requested path is for a static asset
        if os.path.exists(file_path) and not os.path.isdir(file_path):
            return send_from_directory(REACT_BUILD_DIR, path)
        else:
            # For all other paths (React Router routes), send index.html
            return send_from_directory(REACT_BUILD_DIR, 'index.html')

    @app.cli.command("initdb")
    def init_database():
        with app.app_context():
            try:
                db.drop_all() # Clean up existing tables
                db.create_all()
                
                print("Initialized the database.")
            except Exception as e:
                print(f"Error: {e}")

    return app