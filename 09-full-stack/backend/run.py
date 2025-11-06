from app import create_app

# Calls the App Factory to create the Flask application instance
# This 'app' variable is what Gunicorn (and flask run) looks for.
app = create_app()

if __name__ == '__main__':
    app.run()