from .database import add_author, add_post

def seed():
    alice_id = add_author("Alice Johnson", "alice.j@blog.com")
    bob_id = add_author("Bob Smith", "bob.s@blog.com")
    add_post("The Art of ORMs", 
                      "Object-Relational Mappers (ORMs) simplify database interaction by translating object-oriented code into SQL queries.",
                      alice_id)
    add_post("Understanding Flask", 
                      "Flask is a lightweight WSGI web application framework in Python. It's often called a 'micro-framework'.",
                      bob_id)
    add_post("Why Use Cascades?", 
                      "The 'cascade=\"all, delete-orphan\"' option ensures data integrity by automatically deleting related posts when an author is removed.",
                      alice_id)