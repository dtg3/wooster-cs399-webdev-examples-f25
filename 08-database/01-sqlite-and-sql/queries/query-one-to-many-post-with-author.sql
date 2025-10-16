SELECT
	p.title as PostTitle,
	a.username as Author,
	a.email as AuthorEmail
FROM
	posts p
INNER JOIN
	users a ON p.author_id = a.id
ORDER BY
	a.username