# The Flask import
#   The Flask object will be the basis for our web application.
#   Other flask object can be imported too.
from flask import Flask, request, jsonify

# pip install tzdata
from datetime import datetime
from zoneinfo import ZoneInfo


# Creates a flask object using the name of the current source code file
app = Flask(__name__)

# Fake data storage for our application
app.student_data = [
    {
        "id":"12345",
        "firstname":"bruce",
        "lastname":"wayne"
    },
    {
        "id":"67890",
        "firstname":"harleen",
        "lastname":"quinzel"
    },
    {
        "id":"13579",
        "firstname":"bruce",
        "lastname":"banner"
    }
]


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
def hello():
    # Within in route, we can return HTML snippets, JSON,
    #   server generated web pages (templates), etc. For now...just plain
    #   text "Hello!"
    return "HELLO!"


@app.route("/time", methods=['GET'])
def current_time():
    now = datetime.now(ZoneInfo("America/New_York"))
    return f"The time is {now.strftime("%I:%M %p")}"

# Flask supports url variables
#   the default is to treat the variable as a string,
#   but it also supports:
#   * int
#   * path (similar to string, but will accept slashes)
#   * uuid (stands for Universally Unique IDentifier
#       which is a 128-bit number represented as a 36-character
#       alphanumeric string specially suited and formatted for 
#       info identification)
@app.route("/<int:value>")
def doubler(value):
    return jsonify({"input":value,
                   "output":value * 2})


@app.route("/msg", methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        return "POST a request to me with a message!"
    else:
        if request.is_json:
            json_data = request.get_json()
            return f"You sent: {json_data.get('msg')}"
        else:
            form_message = request.form.get('msg')
            return f"You sent: {form_message}"
        

@app.route("/student", methods=['POST'])
def add_student():
    json_data = request.get_json()
    if request.method == 'POST':
        app.student_data.append({'id': str(hash(f"{json_data.get('firstname')}{json_data.get('lastname')}")), 
                                 'firstname': json_data.get('firstname'),
                                 'lastname': json_data.get('lastname')
                                })
        return jsonify(app.student_data[-1])
        

@app.route("/student/<student_id>", methods=['GET', 'PUT', 'PATCH'])
def edit_student(student_id):
        
    target_student = None
    for student in app.student_data:
        if student['id'] == student_id:
            target_student = student

    if not target_student:
        return {'message': f'Cannot find student {student_id}'}, 404

    if request.method == 'GET':
        return jsonify(target_student)

    json_data = request.get_json()
    if request.method == 'PUT':

        if not 'id' in json_data or not 'firstname' in json_data or not 'lastname' in json_data:
            return {'message': f'Incomplete Update'}, 400

        target_student['id'] = json_data.get('id')
        target_student['firstname'] = json_data.get('firstname')
        target_student['lastname'] = json_data.get('lastname')
        return jsonify(target_student)

    if request.method == 'PATCH':
        if not 'id' in json_data and not 'firstname' in json_data and not 'lastname' in json_data:
            return {'message': f'Incomplete Patch'}, 400
        
        if 'firstname' in json_data:
            target_student['firstname'] = json_data.get('firstname')
        
        if 'lastname' in json_data:
            target_student['lastname'] = json_data.get('lastname')

        if 'id' in json_data:
            target_student['id'] = json_data.get('id')
        
        return jsonify(target_student)
    

@app.route("/students")
def get_students():
    if not request.query_string:
     return jsonify(app.student_data)
    
    search = request.args.get('search')
    matches = []
    for student in app.student_data:
        if search in f"{student['firstname']} {student['lastname']}":
            matches.append(student)
    
    return jsonify(matches)
    

    


