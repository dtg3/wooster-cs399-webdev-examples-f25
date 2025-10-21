from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

# Initialize SQLAlchemy instance globally, but configure it in the
# create_app factory function in __init__.py
db = SQLAlchemy()


class Author(db.Model):
    # Define table name
    __tablename__ = 'authors'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Relationship to Posts (posts is a list of Post objects)
    #   Creates a member called author in posts so you can get the author
    #   from a post instance (backref).
    
    #   Lazy waits to load data until you need it. If you don't request it, the
    #   SQL query to get the info won't be executed.
       
    #   The cascade stuff means if you delete an author the posts should also be deleted.
    #   Also, if we remove a post from the authors.posts backref, we need to remove the post
    #   from this table to avoide orphaned data (a post with no author).
    posts = relationship("Post", backref="author", lazy=True, cascade="all, delete-orphan")

    # Conversion of the data to a dictionary for simple JSON transfer.
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

class Post(db.Model):
    
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)

    # Foreign Key for the one-to-many relationship
    #   author_id MUST match the Author model primary key data type (Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author_id': self.author_id,
            
            # Access the author via the relationship
            'author_name': self.author.name if self.author else None 
        }
