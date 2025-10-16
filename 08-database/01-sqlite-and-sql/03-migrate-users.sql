INSERT INTO users (username, email)
SELECT DISTINCT username, email
from raw_blog_data;