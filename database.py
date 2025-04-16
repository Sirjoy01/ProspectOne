import sqlite3

DB_FILE = "prospects.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS distributors (username TEXT PRIMARY KEY)")
    conn.commit()
    conn.close()

def validate_login(distributor):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM distributors WHERE username = ?", (distributor,))
    result = c.fetchone()
    conn.close()
    return result is not None

def get_user_preferences(distributor):
    return {"platform": "Instagram"}

def get_suggestions(distributor, preferences):
    return [{"username": "test_prospect", "platform": "Instagram"}]

def save_contacted(distributor, username):
    pass