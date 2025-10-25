import os
from flask import Flask
from dotenv import load_dotenv
from .routes.api import api_bp
from .models.database import init_db

# Load environment variables from .flaskenv
load_dotenv()

def create_app():
    
    app = Flask(__name__, instance_relative_config=True) 
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass 

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        DATABASE=os.environ.get('DATABASE')
    )

    app.register_blueprint(api_bp)

    @app.cli.command("initdb")
    def init_database():
        with app.app_context():
            try:
                init_db()
            except Exception as e:
                print(f"Error: {e}")

    return app
