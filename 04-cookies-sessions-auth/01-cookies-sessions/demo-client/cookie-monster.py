# Demonstration to illustrate that normal client
#   cookies can be modified by the server AND client
#   there are no safety checks here. Session cookies
#   are cryptographically signed to detect manipulation
#   only the server can modify the data. Client is
#   essentially read only.
import requests

ROOT_URL = "http://127.0.0.1:5000/cookies/demo"

# Here we make a request to the server which creates a cookie,
#   but the client can also initate the cookie creation process.
response = requests.get(ROOT_URL)
cookie_jar = requests.utils.dict_from_cookiejar(response.cookies)
print(response.text)
print(cookie_jar)

# Here, we simply pass the cookie back with a new request
#   the cookie is unmodified.
response = requests.get(ROOT_URL, cookies=cookie_jar)
print(response.text)

# Here, we change the cookie to have a new 'username'
#   this new data is used by the server without issue.
cookie_jar['username'] = 'Boo!'
response = requests.get(ROOT_URL, cookies=cookie_jar)
print(response.text)
