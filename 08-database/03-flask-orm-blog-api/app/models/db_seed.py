# I'm just using this code to start my database with some initial data.
#   It's more interesting than an empty database

# Import the SQLAlchemy instance and models
from .database import db, Author, Post 

def seed_data():
    
    # If we already have authors, the database is
    #   already seeded or at least actively in use
    if Author.query.count() > 0:
        print("Database already seeded. Skipping.")
        return

    print("Seeding database with sample data...")
    
    # We create our Authors just like class instances
    #   in Python.
    author1 = Author(
        name="Alice Johnson",
        email="alice.j@blog.com"
    )    
    author2 = Author(
        name="Bob Smith",
        email="bob.s@blog.com"
    )

    # We can all them all to the session in a list
    db.session.add_all([author1, author2])
    
    # Save the data to the database
    db.session.commit() 
    
    post1 = Post(
        title="The Art of ORMs",
        content="Object-Relational Mappers (ORMs) simplify database interaction by translating object-oriented code into SQL queries.",
        author_id=author1.id  # Use the ID of the committed Author
    )    
    post2 = Post(
        title="Understanding Flask",
        content="Flask is a lightweight WSGI web application framework in Python. It's often called a 'micro-framework'.",
        author_id=author2.id
    )
    post3 = Post(
        title="Why Use Cascades?",
        content="The 'cascade=\"all, delete-orphan\"' option ensures data integrity by automatically deleting related posts when an author is removed.",
        author_id=author1.id
    )
    
    db.session.add_all([post1, post2, post3])
    db.session.commit()
    
    print("Database seeding complete!")
