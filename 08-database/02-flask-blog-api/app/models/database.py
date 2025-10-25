import sqlite3
from flask import current_app, g

# Let's talk about Flask's g object.
#
#   g is Flask's global object. It's a special
#   place where we can store some data unique
#   to our request. We can access this from 
#   anywhere in the application for the life
#   of the request. This makes it an ideal
#   location to store a connection to our
#   database while a request that needs it
#   is made.

# In order to use the database, we need to get
#   a connection to it so we can run the SQL
#   needed to perform our operations.
def get_db():

    # First, we don't want multiple connections to
    #   our database. So if we needed to perform
    #   multiple requests to the database, we ensure
    #   that we only have one active connection.
    #
    #   In this case, db is just the name of the
    #   property we will add to g to hold our database
    #   connection.
    if 'db' not in g:
        # Create the db property in the g object
        #   and establish the database connection.
        g.db = sqlite3.connect(
            current_app.config.get('DATABASE'),
            # This performs the necessary conversions
            #   from the types stored in the database
            #   to appropriate Python types when possible
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # When you execute a query, this will change
        #   the format of the data you are given. By
        #   default the records from a query result are
        #   returned to you as a tuple. This means
        #   field in the record needs to be accessed by
        #   it's numerical position in the tuple. That's
        #   kinda lame and is a pain to deal with. This line
        #   of code makes each each record a SQLite.Row object
        #   which allows records to be accessible like a dictionary
        #   (but they aren't Python dictionaries) so we
        #   can access the data by the name of the field or column.
        g.db.row_factory = sqlite3.Row

        # This will force sqlite to enforce cascades
        #   and foreign key contraints.
        g.db.execute('PRAGMA foreign_keys = ON')
    
    return g.db


# This is registered with the app.teardown_appcontext in __init__.py
#   When a request is done, this teardown gets called and we will
#   cleanup our database connection (if we had one).
#
# Since this is used by Flask during teardown we need an optional
#   parameter for a Flask exception. Often this goes unused, but
#   is required to be used with Flask.
def close_db(e=None):
    # Popping db will remove the connection from g
    db = g.pop('db', None)

    # If we had an actual connection object to the 
    #   database, we'll close it to free up the database.
    if db is not None:
        db.close()


# This function is just used to create the database.
#   We only need to do this once, and instead of it
#   happening each time the application is started,
#   I've tied it to a Flask cli command @app.cli.command("initdb")
#   in __init__.py. This works a lot like a route, but instead of
#   a web request, it's simply a command I can run with Flask. Now
#   if I run flask initdb, this function will get called and create
#   my database. :)
def init_db():
    # Still need a database connection
    db = get_db()
    
    # This sqlite3 library is a very thin wrapper around the database.
    #   We essentially have to connect to the database and tell it we
    #   want to execute SQL commands as strings. When our commands make
    #   changes to the configuration, schema, or data in our tables, we
    #   also need to finish by commiting the changes. The commit is always
    #   done on the database connection object.
    #
    # Enable foreign key enforcement for the current connection
    db.execute('PRAGMA foreign_keys = ON')
    db.commit()
    
    # The cursor object is what we use when we want to run SQL commands
    #   that create or manipulate our tables. This creates that cursor
    #   object. You can think of it like the blinking cursor on your editor
    #   ready to run SQL commands for you. :)
    cursor = db.cursor()

    # Like the execute function on the database connection object,
    #   cursor can also run commands. These again are mostly just
    #   SQL statements. The triple quotes allows us to write them
    #   as multiline strings for convenience and so they look nice. :D
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        );
        """
    )

    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT,
            author_id INTEGER NOT NULL,
            FOREIGN KEY (author_id) REFERENCES authors (id) ON DELETE CASCADE
        );
        """
    )

    # Once we are done having the cursor make our tables, we commit the changes.
    db.commit()


def add_author(name, email):
    """Inserts a new author into the database."""
    db = get_db()
    cursor = db.cursor()

    # This SQL execution looks a little different then before.
    #   The ? marks associated with the VALUES we want are called
    #   Parameterized Queries. We use these rather than something like a
    #   Python f string where we insert the data because these ?
    #   parameters help prevent SQL injection attacks. These parameters
    #   will be properly "escaped" to ensure no one decided to name an
    #   author something like "Bill); DROP TABLE posts; --" without these parameters and
    #   accepting that input as a raw string...you're gonna have a bad day...
    #
    #   This is what causes SQL Injection attacks...don't do that. 
    #   Use the parameterized queries.
    cursor.execute(
        "INSERT INTO authors (name, email) VALUES (?, ?)",
        (name, email)
    )
    db.commit()
    return cursor.lastrowid

def get_all_authors():
    """Fetches all authors from the database."""
    db = get_db()
    # Fetch all will return all the data.
    authors = db.execute("SELECT id, name, email FROM authors").fetchall()
    # Convert all the SQLite Row objects into Python dictionaries
    #   Makes it easy for use to Jsonify our data. :)
    return [dict(author) for author in authors]

def get_author_by_id(author_id):
    
    db = get_db()

    # The query parameters we supply are tuples, so a tuple with
    #   one value needs the extra comma at the end.
    author = db.execute(
        "SELECT id, name, email FROM authors WHERE id = ?",
        (author_id,) 
    ).fetchone() # This will return just one result from a query.
    return dict(author) if author else None

def delete_author_by_id(author_id):

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "DELETE FROM authors WHERE id = ?",
        (author_id,)
    )
    db.commit()
    return cursor.rowcount


def add_post(title, content, author_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO posts (title, content, author_id) VALUES (?, ?, ?)",
        (title, content, author_id)
    )
    db.commit()
    return cursor.lastrowid

def get_all_posts():
    
    db = get_db()
    query = """
    SELECT 
        p.id AS post_id, p.title, p.content, 
        a.id AS author_id, a.name AS author_name, a.email AS author_email
    FROM posts p JOIN authors a ON p.author_id = a.id
    """
    posts = db.execute(query).fetchall()
    return [dict(post) for post in posts]

def get_post_by_id(post_id):
   
    db = get_db()
    query = """
    SELECT 
        p.id AS post_id, p.title, p.content, 
        a.id AS author_id, a.name AS author_name, a.email AS author_email
    FROM posts p JOIN authors a ON p.author_id = a.id
    WHERE p.id = ?
    """
    post = db.execute(query, (post_id,)).fetchone()
    return dict(post) if post else None

def delete_post_by_id(post_id):
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "DELETE FROM posts WHERE id = ?",
        (post_id,)
    )
    db.commit()
    return cursor.rowcount
