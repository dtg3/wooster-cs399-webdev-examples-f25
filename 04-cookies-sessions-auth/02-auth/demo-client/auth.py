import requests
import json
import time


# The base URL for the Flask application. Make sure this matches where your app is running.
BASE_URL = "http://127.0.0.1:5000"

def run_demonstration():
    # Create a requests.Session object. This object will persist cookies
    #   across multiple requests. This simulates how a browser handles sessions.
    with requests.Session() as s:
        print("--- Starting Authentication Demonstration ---")

        # Create a user account
        print("\nCreate a user account...")
        json_data = { "username" : "testuser",
                 "password" : "secretpassword" }
        response = s.post(f"{BASE_URL}/register", json=json_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        time.sleep(2)

        # Attempt to access a protected route without being logged in.
        print("\nAttempting to access the secrets without logging in...")
        response = s.get(f"{BASE_URL}/secret")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        time.sleep(2)

        # Log in with valid credentials.
        print("\nAttempting to log in with 'alice'...")
        login_payload = {"username": "testuser", "password": "secretpassword"}
        response = s.post(f"{BASE_URL}/login", json=login_payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")

        # The session object `s` now holds the session cookie.
        #   We can inspect the cookies to see what the server sent back.
        print(f"Cookies after login: {s.cookies.get_dict()}")
        time.sleep(2)

        # Access the protected route again, now that the session is active.
        print("\nAttempting to access the secrets again, with the session cookie...")
        response = s.get(f"{BASE_URL}/secret")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        time.sleep(2)

        # Log out to end the session.
        print("\nAttempting to log out...")
        response = s.post(f"{BASE_URL}/logout")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        time.sleep(2)

        # Verify that the session is terminated.
        print("\nAttempting to access the secrets one last time after logging out...")
        response = s.get(f"{BASE_URL}/secret")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        print("\n--- Demonstration Complete ---")

if __name__ == "__main__":
    # Make sure your Flask app is running before you run this client script!
    run_demonstration()
