import sqlite3


def connect():
    db = sqlite3.connect("db.sqlite")
    return db

def create_db():
    db = connect()
    cur = db.cursor()
    cur.execute("""CREATE TABLE users (
        user_id INT PRIMARY KEY
    )""")
    db.commit()

def all_block_users():
    db = connect()
    cur = db.cursor()
    return cur.execute(f"""SELECT * FROM users""").fetchall()
    

def add_block_user(user_id):
    db = connect()
    cur = db.cursor()
    cur.execute(f"""INSERT INTO users (user_id) VALUES ({user_id})""")
    db.commit()

def remove_block_user(user_id):
    db = connect()
    cur = db.cursor()
    cur.execute(f"DELETE FROM users WHERE user_id=?", (user_id,))
    db.commit()

try:
    create_db()
except sqlite3.OperationalError:
    pass
