import requests

# Fetch a subject and limit the amount of data returned to 3 items
subject = "science_fiction"
limit = 3

url = f"https://openlibrary.org/subjects/{subject}?limit={limit}"

# This particular API requires us to be specific about what format we want for the data
headers = {"Accept": "application/json"}
response = requests.get(url_header, headers=headers)
books_json = response.json() # This uses the built in json parser from requests

print("\n=== Books fetched using Accept header ===")
for work in books_json["works"]:
    print(f"- {work['title']} by {', '.join(a['name'] for a in work['authors'])}")


# Find the first book (works) from the json
first_work_key = books_json["works"][0]["key"]  # e.g., /works/OL82563W

# Request data about that sepecific book
work_url = f"https://openlibrary.org{first_work_key}"
work_resp = requests.get(work_url, headers=headers)
work_details = work_resp.json()

print("\n=== First book details ===")
print(f"Title: {work_details['title']}")
print(f"Subjects: {', '.join(work_details.get('subjects', []))}")

# Get the author from the book data
first_author_key = work_details["authors"][0]["author"]["key"]  # e.g., /authors/OL2162286A

# Request data about the author
author_url = f"https://openlibrary.org{first_author_key}"
author_resp = requests.get(author_url, headers=headers)
author_details = author_resp.json()

print("\n=== Author details ===")
print(f"Name: {author_details['name']}")
print(f"Birth: {author_details.get('birth_date', 'Unknown')}")
print(f"Top Work: {author_details.get('top_work', 'Unknown')}")
