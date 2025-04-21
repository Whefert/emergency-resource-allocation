import sqlite3
from sqlite3 import Error
from datetime import datetime
import csv

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
        # Create the location table if it doesn't exist
        create_location_table_sql = """
        CREATE TABLE IF NOT EXISTS locations (
            location_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            zone INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        );
        """

        # Create the resource types table if it doesn't exist
        create_resource_types_table_sql = """
        CREATE TABLE IF NOT EXISTS resource_types (
            resource_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        # Create the resources table if it doesn't exist
        create_resource_table_sql = """
        CREATE TABLE IF NOT EXISTS resource (
            resource_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            quantity INTEGER NOT NULL,
  
        );
        """

        # Create the resource type table if it doesn't exist
        create_resource_type_table_sql = """
        CREATE TABLE IF NOT EXISTS resource_type (
            resource_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        # Create priority table if it doesn't exist
        create_priority_table_sql = """
        CREATE TABLE IF NOT EXISTS priority (
            priority_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        conn.execute(create_priority_table_sql)
        print("Property table created or already exists.")

        conn.execute(create_resource_type_table_sql) 

        conn.execute(create_incident_table_sql)
        print("Incident table created or already exists.")

        conn.execute(create_location_table_sql)
        print("Location table created or already exists.")

        conn.execute(create_resource_types_table_sql)
        print("Resource types table created or already exists.")

        conn.execute(create_resource_table_sql)
        print("Resources table created or already exists.")     

        # Close the connection
        conn.close()
        print("Connection closed.")

        return conn
    except Error as e:
        print(e)

    return conn

