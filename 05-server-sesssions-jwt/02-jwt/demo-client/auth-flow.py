import requests
import time

# Base URL for the Flask application
BASE_URL = "http://127.0.0.1:5000/auth"


def register(session, username, password):
    """
    Logs in and gets JWTs via cookies.
    """
    # Use the session to automatically manage cookies
    response = session.post(f"{BASE_URL}/register", json={"username": username, "password": password})
    print(f"{response.text}")


def get_tokens(session, username, password):
    """
    Logs in and gets JWTs via cookies.
    """
    try:
        # Use the session to automatically manage cookies
        response = session.post(f"{BASE_URL}/login", json={"username": username, "password": password})
        response.raise_for_status()
        print(f"\nSUCCESS: {username} logged in! Cookies received.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"\nERROR: Login failed: {e}")
        return False


def access_protected(session):
    """
    Tries to access the protected route.
    It retrieves the CSRF token from the cookie and sends it in the header.
    """
    # Get the CSRF token from the session's cookies.
    csrf_token = session.cookies.get("csrf_access_token")
    if not csrf_token:
        print("\nERROR: No CSRF token found in cookies. Cannot access protected route.")
        return None

    headers = {"X-CSRF-TOKEN": csrf_token}
    try:
        response = session.get(f"{BASE_URL}/protected", headers=headers)
        response.raise_for_status()
        print("\nSUCCESS: Protected route accessed")
        print(response.json())
        return response
    except requests.exceptions.HTTPError as e:
        print(f"\nERROR: Protected route access failed: {e}")
        try:
            print(response.json())
        except requests.exceptions.JSONDecodeError:
            print("ERROR: Response content is not JSON.")
        return None


def refresh_token(session):
    """
    Refreshes the access token using a refresh token.
    CSRF token for refresh is automatically managed by `requests.Session`.
    """
    # The refresh endpoint is also CSRF-protected.
    csrf_token = session.cookies.get("csrf_refresh_token")
    if not csrf_token:
        print("\nERROR: No refresh CSRF token found. Cannot refresh.")
        return None

    headers = {"X-CSRF-TOKEN": csrf_token}
    try:
        response = session.post(f"{BASE_URL}/refresh", headers=headers)
        response.raise_for_status()
        print("\nSUCCESS: Access token refreshed. New cookies received.")
        print(response.json())
        return True
    except requests.exceptions.HTTPError as e:
        print(f"\nERROR: Token refresh failed: {e}")
        try:
            print(response.json())
        except requests.exceptions.JSONDecodeError:
            print("ERROR: Response content is not JSON.")
        return False


def logout(session):
    """
    Logs out and unsets the JWT cookies.
    """
    try:
        response = session.post(f"{BASE_URL}/logout")
        response.raise_for_status()
        print("\nSUCCESS: Logged out. Cookies are now unset.")
    except requests.exceptions.RequestException as e:
        print(f"\nERROR: Logout failed: {e}")


def display_cookies(cookies):
    for cookie in cookies:
        print(f"Cookie Name: {cookie.name}")
        print(f"Cookie Value: {cookie.value}") # This might be empty or a placeholder for HttpOnly cookies
        print(f"HttpOnly: {'HttpOnly' in cookie._rest}")
        print("-" * 20)


def main():
    # Timeouts to test if the token system is working
    #   all values in seconds.
    jwt_lifetime = 15 
    jwt_refresh_lifetime = 45

    # Use a session object to handle cookies automatically
    session = requests.Session()

    print("--- Register a User ---")
    register(session, "testuser", "password123")

    # 1. Login and get initial cookies
    print("--- Step 1: Logging in with valid credentials ---")
    if not get_tokens(session, "testuser", "password123"):
        return
    
    display_cookies(session.cookies)
    print(session.headers)

    # 2. Access the protected route immediately
    print("\n--- Step 2: Accessing protected route with fresh access and CSRF token ---")
    access_protected(session)
    
    display_cookies(session.cookies)
    print(session.headers)

    # 3. Simulate a time lapse
    print("\n--- Step 3: Waiting to simulate access token expiration (but not refresh token) ---")
    print("Note: The actual token lifetime is 15 minutes, but we simulate a short wait for the demo.")
    time.sleep(jwt_lifetime)

    # 4. Attempt to refresh the access token
    print("\n--- Step 4: Using the refresh token to get a new access token and CSRF token ---")
    if not refresh_token(session):
        print("Refresh failed, cannot continue.")
        return
    
    display_cookies(session.cookies)
    print(session.headers)

    # 5. Access the protected route with the newly refreshed access token
    print("\n--- Step 5: Accessing protected route with the newly refreshed token and new CSRF header ---")
    access_protected(session)

    
    # 6. Everything has expired
    #   If both the access and refresh tokens are expired this should fail.
    print("\n--- Step 6: Wait for access and refresh tokens to expire. ---")
    time.sleep(jwt_refresh_lifetime)
    print("\n--- Step 6.1: Try to refresh with the expired refresh token which should fail. ---")
    refresh_token(session)
    print("\n--- Step 6.2: Try to access the protected route which should also fail. ---")
    access_protected(session)
    display_cookies(session.cookies)
    print(session.headers)

    # 7. Logout to clear the cookies
    print("\n--- Step 7: Logging out ---")
    logout(session)

if __name__ == "__main__":
    main()
