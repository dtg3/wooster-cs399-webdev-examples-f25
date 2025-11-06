import pytest

from app import create_app
from app import db

TEST_DATABASE_URI = 'sqlite:///:memory:'

from app.models.database import create_post

@pytest.fixture
def app():
    app = create_app()

    app.config.update({
        'SQLALCHEMY_DATABASE_URI': TEST_DATABASE_URI
    })

    # Initialize the test database schema and populate it
    with app.app_context():
        db.create_all()
        
    yield app

    # Teardown: Close the session, drop tables
    with app.app_context():
        db.session.remove() # Close the session
        db.drop_all() # Clean up (less critical for :memory: but good practice)

@pytest.fixture
def create_test_post(app):
    def _create_test_post(title="Test Post Title", content="Test post content."):
        with app.app_context():
            new_post = create_post(title=title, content=content)
            return new_post.id
    return _create_test_post

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def db_conn(app):
    with app.app_context():
        yield db.session 
        db.session.rollback()
        db.session.remove()