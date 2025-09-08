# A simple appliation to show session based authentication
#   This is not a good way to implement it, but some of the
#   ideas will carry over into our other talks on authenticating
#   with a server-session. For now, enjoy being able to login :)
from flask import Flask

import os

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    # A mock "database" of users for demonstration purposes.
    #   In a real application, this would be a secure database lookup.
    app.users = {}

    from .routes.routes_bp import routes_bp
    app.register_blueprint(routes_bp)

    return app
