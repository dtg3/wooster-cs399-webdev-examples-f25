import sqlite3
import os
from flask import current_app

def get_db():
    db_path = os.path.join(current_app.instance_path, current_app.config.get("DATABASE"))
    conn = sqlite3.connect(
        db_path,
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    sql_create_table = """
    DROP TABLE IF EXISTS tasks;
    CREATE TABLE tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    );
    """
    cursor.executescript(sql_create_table)
    conn.commit()
    conn.close()


def get_tasks(task_id=None):
    print(f"database: {task_id}")
    conn = get_db()
    cursor = conn.cursor()

    if not task_id:
        tasks = cursor.execute("SELECT id, description, completed FROM tasks ORDER BY id;").fetchall()
        return [] if not tasks else [dict(task) for task in tasks] 

    result = cursor.execute("SELECT id, description, completed FROM tasks WHERE id = ?;", (task_id,)).fetchone()

    conn.close()
    return [] if not result else [dict(result)]


def insert_task(description, completed=0):
    conn = get_db()
    cursor = conn.cursor()

    insert_sql = "INSERT INTO tasks (description, completed) VALUES (?, ?);"
    # SQLite stores booleans as 0 (False) or 1 (True)
    completed_int = 1 if completed else 0

    cursor.execute(insert_sql, (description, completed_int))
    conn.commit()
    
    # Get the id for the newly entered task
    #   only works for numeric id's like an autonumber or a
    #   numeric ID generate with code. It will NOT work if you
    #   use something like a UUID, string, or have a composite key
    #   (a primary key made up of two attributes)
    lastrowid = cursor.lastrowid

    conn.close()
    return lastrowid


def update_task(task_id, description, completed):
    # Convert Python bool to SQLite integer
    completed_int = 1 if completed else 0

    conn = get_db()
    cursor = conn.cursor()
    
    update_sql = """
    UPDATE tasks 
    SET description = ?, completed = ?
    WHERE id = ?
    """

    cursor.execute(update_sql, (description, completed_int, task_id))
    conn.commit()

    # Returns the number of rows affected
    rowcount = cursor.rowcount

    conn.close()
    
    return rowcount


def delete_task(task_id):
    conn = get_db()
    cursor = conn.cursor()

    query = "DELETE FROM tasks WHERE id = ?"
    cursor.execute(query, (task_id,))
    conn.commit()
    conn.close()

    