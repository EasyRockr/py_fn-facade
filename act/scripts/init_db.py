# scripts/init_db.py
import sqlite3
from pathlib import Path

# Path to the DB (same location the DAL expects)
DB_PATH = Path(__file__).resolve().parent.parent / "address_book1.db"

def init_db():
    """Create the database file and populate it with sample contacts."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Drop + recreate the contacts table
    cur.executescript("""
    DROP TABLE IF EXISTS contacts;
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact TEXT NOT NULL
    );
    """)

    # Insert sample data
    cur.executemany(
        "INSERT INTO contacts (name, contact) VALUES (?, ?);",
        [
            ("Jane Doe", "+6882345678910"),
            ("John Doe", "+7882345678910")
        ]
    )

    conn.commit()
    conn.close()
    print(f"Database initialized at: {DB_PATH}")

if __name__ == "__main__":
    init_db()
