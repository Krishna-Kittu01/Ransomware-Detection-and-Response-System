import sqlite3
import os

DB_PATH = "data/rdrs.db"


def init_database():
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS file_events (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            filename TEXT,

            event_type TEXT,

            entropy REAL,

            status TEXT,

            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()

    conn.close()

    print("✅ Database initialized successfully.")


def insert_event(filename, event_type, entropy, status):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO file_events
        (filename, event_type, entropy, status)
        VALUES (?, ?, ?, ?)
    """, (filename, event_type, entropy, status))

    conn.commit()

    conn.close()