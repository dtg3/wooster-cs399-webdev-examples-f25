# Built-in Python Library for Handling Json Data
#   * Can read from strings/files
#   * Loads JSON object in memory
#   * Can treat the in memory object like Python Lists/Dictionaries
import json

# Third-party Library for making web requests and receiving the responses
#   Does have a built in json parser
import requests


# Request the College of Wooster website
cow_website = requests.get('https://college-of-wooster-cs.github.io/')

# Response Result
print(f"STATUS CODE: {cow_website.status_code}", end="\n\n")

# Response Headers
print(f"HEADERS:\n{cow_website.headers}", end="\n\n")

# Response Body
print(f"RESPONSE BODY:\n{cow_website.text}", end="\n\n")

# Request to an the OpenLibrary API
# Configure the headers of the request to say that we only want JSON data
headers = {'Accept': 'application/json'}
open_library = requests.get('https://openlibrary.org/subjects/computers?limit=2', headers=headers)

# Response Result
print(f"STATUS CODE: {open_library.status_code}", end="\n\n")

# Response Headers
print(f"HEADERS:\n{open_library.headers}", end="\n\n")

# Response Body
json_data = json.loads(open_library.text)
print(f"RESPONSE BODY:\n{json.dumps(json_data, indent=4)}", end="\n\n")

for book in json_data['works']:
    print(book["title"])