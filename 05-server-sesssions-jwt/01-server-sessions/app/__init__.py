import os

from flask import Flask
from flask_login import LoginManager, UserMixin
from flask_session import Session


# --- User Model for Flask-Login ---
# The User class is a required part of Flask-Login. It must inherit from UserMixin
#   and provide a `get_id()` method to help Flask-Login manage the user session.
class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def get_id(self):
        # This method is used by Flask-Login to get the unique identifier for the user.
        # This ID is what gets stored in the server-side session.
        return str(self.id)


# This is how we will determine if users are authenticated
#   and thus authorized to view protected routes
login_manager = LoginManager()

# This is different than the regular session object that comes with flask.
#   This actually implements server side sessions and not just all the data
#   in a signed cookie.
app_sesssion = Session()

def create_app():

    app = Flask(__name__)

    # This will hold our users to simulate a database
    app.users = {}
    
    # You need this to sign your cookies!
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
 
    # With Flask-Session the client will only receive a secure session ID cookie.
    #   All session data will be stored on our filesystem to simulate either a database
    #   or caching solution. This signs the cookie to detect tampering and makes a
    #   session permanent until server restart. We'll also clear the session in
    #   the route /logout.
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["SESSION_FILE_DIR"] = "./flask_session_cache" 
    app.config["SESSION_PERMANENT"] = True 

    
    # Add login management from Flask-Login
    login_manager.init_app(app)
    # Initialize the Flask-Session extension
    #   This step overrides Flask's default session behavior.
    app_sesssion.init_app(app)


    # --- User Loader and Unauthorized Handlers ---
    #  The user_loader callback tells Flask-Login how to load the
    #   user object from the user ID stored in the server-side session.
    #   It is called on every request to a protected route.
    @login_manager.user_loader
    def load_user(user_id):
        if user_id in app.users:
            return User(id=user_id)
        return None


    # The unauthorized_handler callback is triggered when a user tries to access a
    #   route with `@login_required` without being logged in. We return a JSON response
    #   with a 401 Unauthorized status code, which is standard for APIs.
    @login_manager.unauthorized_handler
    def unauthorized():
        return {"message": "Unauthorized. Please log in."}, 401


    # We import and register the routes blueprint here
    from .routes.routes_bp import routes_bp
    app.register_blueprint(routes_bp)

    # A little starting "index" route :)
    @app.route('/')
    def demo_index():
        return "Authentication with Server-Sessions"
    
    return app
