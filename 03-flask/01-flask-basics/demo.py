# This is the minimal import to use flask
#   The Flask object will be the basis for our web application
from flask import Flask

# Creates a flask object using the name of the current source code file
app = Flask(__name__)

# This is a route that defines how or application should responsd
#   to requests it receives.
#  
# The @ symbol indicates a decorator. A simple way to think
#   of this is we are wrapping our function index() within
#   the route() function provided by the decorator. This means
#   route() augments our index() function to perform the necessary
#   actions so our index() function is called when we make a request
#   for the the root ("/") of our web app/service.
#
# If you'd like to learn more about Python decorators
#   
#   https://www.geeksforgeeks.org/python/decorators-in-python/#
#   https://realpython.com/primer-on-python-decorators/
#
# You'll see decorators again for other aspects of the course, but I
#   only expect that you know when and how to use them in this context.
#   I will not ask you to implement a decorator using Python on an exam.

@app.route("/")
def index():
    # Within in route, we can return HTML snippets, JSON,
    #   server generated web pages, etc. For now...just plain
    #   text "Hello!"
    return "HELLO!"
