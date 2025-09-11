import requests
import time

BASE_URL = "http://127.0.0.1:5000"

# The requests Session object automatically handles cookies.
session = requests.Session()


def register():
    print("--- Create a user account ---")
    register_url = f"{BASE_URL}/register"
    credentials = {"username": "testuser", "password": "password123"}
    response = session.post(register_url, json=credentials)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 25)
    time.sleep(1)


def login():
    print("--- Attempting to log in ---")
    login_url = f"{BASE_URL}/login"
    credentials = {"username": "testuser", "password": "password123"}
    response = session.post(login_url, json=credentials)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 25)
    time.sleep(1)


def get_profile():
    print("--- Getting profile data ---")
    profile_url = f"{BASE_URL}/profile"
    response = session.get(profile_url)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 25)
    time.sleep(1)


def update_profile():
    print("--- Updating protected profile message ---")
    profile_url = f"{BASE_URL}/profile"
    new_message = {"profile_message": "My new profile message!"}
    response = session.put(profile_url, json=new_message)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 25)
    time.sleep(1)


def get_public_endpoint():
    print("--- Accessing public endpoint ---")
    public_url = f"{BASE_URL}/public"
    response = session.get(public_url)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 25)
    time.sleep(1)


def logout():
    print("--- Attempting to log out ---")
    logout_url = f"{BASE_URL}/logout"
    response = session.post(logout_url)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 25)
    time.sleep(1)


if __name__ == "__main__":
    print("--- Starting client-server interaction ---")

    # Register a new user
    register()

    # Access a protected resource without being logged in (should fail)
    get_profile()

    # Log in
    login()

    # Access the protected profile page again (should succeed)
    get_profile()

    # Update the profile message
    update_profile()

    # Get the profile again to confirm the update
    get_profile()

    # Access a public endpoint (always works)
    get_public_endpoint()

    # Log out to end the session
    logout()

    # ry to access the protected resource again (should fail)
    get_profile()

    print("--- Client interaction complete ---")