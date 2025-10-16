INSERT INTO tags (name)
SELECT DISTINCT tag_name
FROM raw_blog_data;