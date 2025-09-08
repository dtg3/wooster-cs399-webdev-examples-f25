from flask import Blueprint, request, session, redirect, url_for

session_demo = Blueprint("sessions", __name__)

@session_demo.route("/")
def index():
    return "Session Demo!"
    
    
@session_demo.route("/demo")
def session_maker():
    
    # Checks to see if a session exists
    if session:
        return f"{session['s_user']} you already have a session!"
    
    # If not, let's make the cookie and create a space to store some data
    session['s_user'] = 'batman'
    session['data'] = []

    # This lets us work the redirect in the event that we try to add a value
    #   before the cookie is made
    next_url = request.args.get('next')
    
    # Call the redirect
    if next_url:
        return redirect(next_url)
    
    return f"Created a session for {session['s_user']}"

    
@session_demo.route("/add/<value>")
def update_session(value):

    # if we didn't make a session or the 
    #   data field 's_user' isn't in the session
    #   we will redirect to the the /demo route using session_maker
    #   and then tell session_maker to bring us back here when it's done.
    if not session or 's_user' not in session:
        # The url_for() can pass url variables
        return redirect(url_for('sessions.session_maker', next=url_for('sessions.update_session', value=value)))
    
        # An alternative solution is to simply pass the request's path which should include the value also
        #return redirect(url_for('sessions.session_maker', next=request.path))

    # Add the data to the session
    data_items = session['data']
    data_items.append(value) 
    session['data'] = data_items

    return f"{value} added to session"


@session_demo.route("/print")
def display_session_data():
    session_data = []
    for key, value in session.items():
        session_data.append(f"{key}:{value}<br>")
    
    return ''.join(session_data)


@session_demo.route("/done")
def end_session():
    session.clear() # Deletes all session data in the client cookie
    return "Session Emptied!"
        
