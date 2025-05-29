import sqlite3
import json
from passlib.hash import bcrypt

DB_PATH = "users.db"

# Initialize or update database schema
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # users table (login credentials)
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

    # meal_plans table (saved meal plans per user)
    c.execute("""
      CREATE TABLE IF NOT EXISTS meal_plans (
        username   TEXT,
        plan_text  TEXT,
        timestamp  DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    """)

    conn.commit()
    conn.close()

# User management
def create_user(username: str, password: str) -> bool:
    """Create a new user. Return False if the username already exists."""
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
    """Verify a user's login credentials."""
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

# Profile management (BMR + allergies)
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
        (username, bmr, allergies_json)
    )
    conn.commit()
    conn.close()


def load_profile(username: str):
    """Return (bmr, [allergies]) or (None, []) if no profile exists."""
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
    allergies = json.loads(allergies_json or "[]")
    return bmr, allergies

# Meal plan management (saved meal plans per user)
def save_meal_plan(username: str, plan_text: str):
    """Save a generated meal plan for the user."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO meal_plans (username, plan_text) VALUES (?, ?)",
        (username, plan_text)
    )
    conn.commit()
    conn.close()


def load_meal_plans(username: str, limit: int = 5):
    """Fetch the most recent meal plans for the user."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "SELECT plan_text, timestamp FROM meal_plans "
        "WHERE username = ? "
        "ORDER BY timestamp DESC LIMIT ?",
        (username, limit)
    )
    rows = c.fetchall()
    conn.close()
    return rows
