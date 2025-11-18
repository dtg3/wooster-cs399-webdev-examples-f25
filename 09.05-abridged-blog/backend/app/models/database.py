from datetime import datetime
from .. import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now)
    modified_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'<POST(id={self.id}, title={self.title},create_at={self.created_at}, modified_at={self.modified_at})>'
    
    def to_dict(self):
        return {'id': self.id,
                'title': self.title,
                'content': self.content,
                'created_at': self.created_at.isoformat() if self.created_at else None,
                'modified_at': self.modified_at.isoformat() if self.modified_at else None
        }
    
def create_post(title, content):
    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()
    return new_post

def get_all_posts():
    stmt = db.select(Post).order_by(Post.created_at.desc())
    return db.session.execute(stmt).scalars().all()

    
