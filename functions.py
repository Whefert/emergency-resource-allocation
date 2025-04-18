import sqlite3
from sqlite3 import Error
from datetime import datetime

def create_connection(db_name):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        print(f"Connected to database: {db_name}")

        # Create incident table if it doesn't exist
        create_incident_table_sql = """
        CREATE TABLE IF NOT EXISTS incidents (
            incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        conn.execute(create_incident_table_sql)
        print("Incident table created or already exists.")

        

        return conn
    except Error as e:
        print(e)

    return conn

