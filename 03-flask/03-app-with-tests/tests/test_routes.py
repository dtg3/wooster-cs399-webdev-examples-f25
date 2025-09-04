# This function is run by pytest. 
#   The functions will all be named "test_".
#   The function takes one parameter which is the
#   client or web application which is passed from
#   our conftest.py setup fixture.
def test_hello_route(client):

    # Similar to the requests library in Python, the client
    #   can perform requests of the Flask web app, and provide
    #   a response.
    response = client.get("/hello")

    # Responses can then be evaluated to see if they match the
    #   applications specifications. Assert statements here are
    #   what we use to confirm the code is behaving correctly.
    #   An assert only passes if the result of the statement that
    #   follows it evaluates to True. If the assert receives False
    #   the test has failed.
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Flask Factory!"}
