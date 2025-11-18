import os
from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .routes.time_api import time_bp
from .routes.posts_api import posts_bp

# Load environment variables from .flaskenv
load_dotenv()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    if os.environ.get('FLASK_ENV') == 'development':
        CORS(app)


    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI='sqlite:///' + 
            os.path.join(app.instance_path, os.environ.get('DATABASE', 'blog.db')),
        SQLALCHEMY_TRACK_MODIFICATION=False
    )
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    
    app.register_blueprint(time_bp)
    app.register_blueprint(posts_bp)

    @app.route('/')
    def home():
        return "FOOBAR!!!!!"

    @app.cli.command("initdb")
    def init_database():
        with app.app_context():
            try:
                db.drop_all()
                db.create_all()
                print("Init successful")
            except Exception as e:
                print(f"Error: {e}")

    return app