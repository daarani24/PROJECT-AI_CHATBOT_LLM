import sqlite3

DB_NAME = "chatbot.db"


def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_message(role, message):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chat_history(role,message) VALUES(?,?)",
        (role, message)
    )

    conn.commit()
    conn.close()

def load_messages():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT role,message FROM chat_history"
    )

    data = cursor.fetchall()
    conn.close()
    return data

def clear_database():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM chat_history")

    conn.commit()
    conn.close()