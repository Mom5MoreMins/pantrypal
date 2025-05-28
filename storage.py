# storage.py
import sqlite3
from passlib.hash import bcrypt

DB_PATH = "users.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # users table
    c.execute("""
      CREATE TABLE IF NOT EXISTS users (
        username      TEXT PRIMARY KEY,
        password_hash TEXT NOT NULL
      )
    """)
    conn.commit()
    conn.close()

def create_user(username: str, password: str) -> bool:
    """Return False if username exists, else hash & store and return True."""
    pw_hash = bcrypt.hash(password)
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, pw_hash)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(username: str, password: str) -> bool:
    """Return True if username exists and password matches."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username,)
    )
    row = c.fetchone()
    conn.close()
    if not row:
        return False
    return bcrypt.verify(password, row[0])
