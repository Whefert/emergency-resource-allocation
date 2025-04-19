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



        conn.execute(create_incident_table_sql)
        print("Incident table created or already exists.")

        conn.execute(create_location_table_sql)
        print("Location table created or already exists.")

        conn.execute(create_resource_types_table_sql)
        print("Resource types table created or already exists.")

        conn.execute(create_resource_table_sql)
        print("Resources table created or already exists.")     

        conn.execute(create_resource_type_table_sql) 

        return conn
    except Error as e:
        print(e)

    return conn

def seed_resource_types(conn):
    # Raead the CSV file in the data folder and insert data into the resource_types table
    # Assuming the CSV file has columns: name, description
    try:
        with open('data/resource_types.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            sql = '''INSERT INTO resource_types (name, description) VALUES (?, ?)'''
            cur = conn.cursor()
            cur.executemany(sql, reader)
            conn.commit()
            print("Resource types seeded successfully.")
    except Error as e:
        print(e)


    """ Seed the resource types table with initial data """
    try:
        sql = '''INSERT INTO resource_types (name, description) VALUES (?, ?)'''
        resource_types = [
            ('Type1', 'Description for Type1'),
            ('Type2', 'Description for Type2'),
            ('Type3', 'Description for Type3')
        ]
        cur = conn.cursor()
        cur.executemany(sql, resource_types)
        conn.commit()
        print("Resource types seeded successfully.")
    except Error as e:
        print(e)