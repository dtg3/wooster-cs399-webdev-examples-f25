# This conftest.py file is used to setup and
#   configure testing for your flask application.
#   All tests are in the tests folder and each test
#   file is prefixed with "test_". These are run
#   automatically when running the full test suite.
#   The pytest application can also run subsets of
#   the test suite.

# Testing is run with the command
#   pytest
# This command must be run from the root of the
#   project directory (where conftest.py is located)

# Pytest is a popular testing framework for
#   Python programs. We will use it here along
#   side our Flask backend API to ensure that
#   the features work as planned.
import pytest
from app import create_app


# Fixtures are the way PyTest sets things up for 
#   running tests. This app function is a special
#   fixture that starts up flask in testing mode
#   The yield keyword here turns our function into
#   a generator. Essentially, the function sends the 
#   requested data, and saves is state so that it can
#   be resumed. For our purposes code before the yield
#   is for testing setup, and code after the yield is
#   "teardown" or cleaning up the testing.
#
# This function can also be envoked as a parameter for 
#   a pytest so that you can utilze the applications context.
#   For example, this would be useful if you needed to test
#   that database actions are working properly.
@pytest.fixture
def app():
    app = create_app()
    app.config.update({"TESTING": True})
    yield app


# Flask has two methods of interaction. One is the normal
#   web application client. This fixture creates that object
#   and hand it off to tests that need it.
@pytest.fixture
def client(app):
    return app.test_client()


# Flask also supports creating command line functions that can
#   be used for setup/deployment or any other thing your application
#   might need. This example won't use this fixture, but it's
#   presented here for completeness.
@pytest.fixture
def runner(app):
    return app.test_cli_runner()
