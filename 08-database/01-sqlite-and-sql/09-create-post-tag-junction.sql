DROP TABLE IF EXISTS posts_tags_junct;

CREATE TABLE posts_tags_junct (
    post_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    
    -- The combination of these two is the Compound Primary Key
    PRIMARY KEY (post_id, tag_id), 
    
    FOREIGN KEY (post_id) REFERENCES posts (id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags (id) ON DELETE CASCADE
);