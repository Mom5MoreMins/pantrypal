import sqlite3
import json
from passlib.hash import bcrypt

DB_PATH = "users.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # users table (login)
    c.execute("""
      CREATE TABLE IF NOT EXISTS users (
        username      TEXT PRIMARY KEY,
        password_hash TEXT NOT NULL
      )
    """)

    # user_profiles table (BMR + allergies)
    c.execute("""
      CREATE TABLE IF NOT EXISTS user_profiles (
        username  TEXT PRIMARY KEY,
        bmr       REAL,
        allergies TEXT
      )
    """)

    conn.commit()
    conn.close()

def create_user(username: str, password: str) -> bool:
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

def save_profile(username: str, bmr: float, allergies: list[str]):
    """Insert or update the user’s BMR and allergy list."""
    allergies_json = json.dumps(allergies)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO user_profiles (username, bmr, allergies)
        VALUES (?, ?, ?)
        ON CONFLICT(username) DO UPDATE SET
          bmr = excluded.bmr,
          allergies = excluded.allergies
        """,
        (username, bmr, allergies_json),
    )
    conn.commit()
    conn.close()

def load_profile(username: str):
    """Return (bmr, [allergies]) or (None,[]) if none saved."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "SELECT bmr, allergies FROM user_profiles WHERE username = ?",
        (username,)
    )
    row = c.fetchone()
    conn.close()
    if not row:
        return None, []
    bmr, allergies_json = row
    allergies = json.loads(allergies_json) if allergies_json else []
    return bmr, allergies
