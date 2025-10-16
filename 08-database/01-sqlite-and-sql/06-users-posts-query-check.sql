SELECT 
	u.username AS author,
	p.title AS title,
	p.content AS content
FROM
	posts p
INNER JOIN
	users u ON p.author_id = u.id;
