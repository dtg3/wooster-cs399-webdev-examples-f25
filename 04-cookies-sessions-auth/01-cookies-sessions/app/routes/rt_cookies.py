from flask import Blueprint, request, make_response

cookie_demo = Blueprint("cookies", __name__)

@cookie_demo.route("/")
def index():
    return "Cookie Demo!"

@cookie_demo.route("/demo")
def cookie_maker():
    
    # Sometimes we need more information to be returned with a response
    #   this might be headers for metadata or additional data for the client
    #   and server in the form of COOKIES!
    #  
    # Cookies hold data like JSON objects. You can store Strings, Numbers,
    #   Booleans, (JSON) Objects, and (JSON) Arrays.
    # 
    # COOKIES DO HAVE OTHER PRACTICAL LIMITATIONS
    #   * You are limited to the number of cookies your app can store (usually 100s)
    #   * Cookies can only be about 4KB in size
    #   * Cookies are sent with EVERY REQUEST. The more you have/larger they are
    #       the larger performance overhead and latency on requests.
    #   We can work around some of these limitations if we consider alternative storage methods
    #       ( To be continued in a Local Storage discussion :) ).
    # 
    
    # Here we will check to see if a cookie already exists
    #   and has been sent along with the request. For this
    #   example, we don't want to change it!
    username_cookie = request.cookies.get('username')

    if not username_cookie:
        # Create a response object with the string as the body
        #   This will simply create the object and the argument
        #   will be the body of the response.
        response = make_response("Cookie Created!")


        # Let's add some data to our cookie
        #   The age of our cookie will last for 2 minutes
        #   or 120 seconds.
        response.set_cookie('username', 'Drew', max_age=120)

        # Let's send our response back!
        return response
    
    return f"Welcome back, {username_cookie}!"
