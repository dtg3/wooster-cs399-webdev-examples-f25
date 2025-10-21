INSERT INTO tags (name)
SELECT DISTINCT tag_name
FROM raw_blog_data;

--Insert a tag that isn't used by any posts
--  Used to demonstrate a query later
INSERT INTO tags (name) VALUES
('Haskell');