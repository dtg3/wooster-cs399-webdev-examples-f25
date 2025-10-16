--INSERT INTO posts (author_id, title, content, created_at)
SELECT 
	a.id as author_id,
	---a.username,
	r.post_title as title,
	r.post_content as content,
	r.created_at as created_at
FROM 
	raw_blog_data r
INNER JOIN 
	users a ON r.username = a.username 
GROUP BY 
	r.post_id;