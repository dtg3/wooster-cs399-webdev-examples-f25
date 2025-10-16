SELECT
    p.title AS PostTitle,
	u.username AS Author,
	p.created_at AS PublishDate,
    t.name AS TagName
FROM
	tags t
INNER JOIN
    posts_tags_junct ptj ON t.id = ptj.tag_id
INNER JOIN
    posts p ON ptj.post_id = p.id
INNER JOIN
    users u ON p.author_id = u.id
WHERE
    t.name = 'Python'
ORDER BY
	p.created_at DESC;
