# Import that implicitly runs our __init__.py code
from app import create_app

# Flask app is ready to go!
app = create_app()
