from datetime import datetime
from .. import db

# SQLAlchemy Model
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.now)
    modified_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    def __repr__(self):
        return f'<Post(id={self.id}, title={self.title}, created_at={self.created_at}, modified_at={self.modified_at}>'
        
    # Helper to convert to a dictionary for API responses
    def to_dict(self):
        return {'id': self.id,
                'title': self.title,
                'content': self.content,
                # Using isoformat ensures clean, standard timestamp strings in JSON
                'created_at': self.created_at.isoformat() if self.created_at else None,
                'modified_at': self.modified_at.isoformat() if self.modified_at else None
                }


# Data Access Layer Functions (DAL)

def create_post(title, content):
    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()
    return new_post

def get_post_by_id(post_id):
    return db.session.get(Post, post_id)

def update_post(post_id, title=None, content=None):
    post_data = db.session.get(Post, post_id)
    if post_data is None:
        return 0 # Post not found
    
    changed = False
    
    if title is not None and title != post_data.title:
        post_data.title = title
        changed = True
    
    if content is not None and content != post_data.content:
        post_data.content = content
        changed = True
        
    if changed:
        db.session.commit()
        return 1
    else:
        # Post was found, but no changes were made
        return 0

def delete_post(post_id):
    # Simple way to get a post object by it's ID
    post_to_delete = db.session.get(Post, post_id)
    
    if post_to_delete is None:
        return 0 # Post not found
        
    db.session.delete(post_to_delete)
    db.session.commit()
    return 1 # One row deleted

def get_posts_by_title(title):
    # Let's unpack this stuff...
    # We have really nice queries to get a piece of information when we
    #   know the ID, but sometimes more complex queries are necessary.
    #   For this, we can use the database object to assemble a query
    #   which looks similar to SQL, but more "Object"-like. So once
    #   we have a statement assembled, we can ask our database session
    #   execute the query.
    stmt = db.select(Post).where(Post.title == title)

    # A resonable follow-up is what the heck is "scalars" used for?
    #   Well, for this query I only need one type of Object, my Posts.
    #   The way results are returned are rows of tuples. So if we make
    #   a query that uses data from only one table, each row is a tuple
    #   of object (the data from that table). If we were to do a join on
    #   multiple tables, then the data gets more complex and each row
    #   will have tuples with more than one object type. When you have
    #   data from one table like I do here, it's awkward to work with 
    #   a list of tuples where every tuple is only one value. The folks
    #   who made SQLAlchemy decided that to help with that, the scalars()
    #   will collapse data like this from one Object/Table into a list of
    #   each object (or rows of data from the table). IF YOU DO A JOIN OVER
    #   MULTIPLE TABLES OF DATA, DO NOT USE SCALARS.
    return db.session.execute(stmt).scalars().all()

def get_all_posts():
    stmt = db.select(Post).order_by(Post.created_at.desc())
    return db.session.execute(stmt).scalars().all()