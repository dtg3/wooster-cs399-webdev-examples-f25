from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    
    # This will be used to sign our session cookies!
    #   You need to add a SECRET_KEY TO YOUR .flaskenv
    #   it can be anything, but using the README instructions
    #   will give you a secure key.
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    from .routes.rt_cookies import cookie_demo
    from .routes.rt_session import session_demo
    app.register_blueprint(cookie_demo, url_prefix='/cookies')
    app.register_blueprint(session_demo, url_prefix='/sessions')

    @app.route('/')
    def demo_index():
        return "Cookie and Session Demos"
    
    return app
