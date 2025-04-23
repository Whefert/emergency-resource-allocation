import sqlite3
from sqlite3 import Error
from datetime import datetime
import csv


# TODO: Create a function to create the database separate from create the connec


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
        CREATE TABLE IF NOT EXISTS location (
            location_id INTEGER PRIMARY KEY AUTOINCREMENT,
            zone INTEGER NOT NULL,
            x_coordinate INTEGER NOT NULL,
            y_coordinate INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        # Create the resources table if it doesn't exist
        create_resource_table_sql = """
        CREATE TABLE IF NOT EXISTS resource (
            resource_id INTEGER PRIMARY KEY AUTOINCREMENT,
            resource_type_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (resource_type_id) REFERENCES resource_type (resource_type_id)
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

        # Create emergency types table if it doesn't exist
        create_emergency_type_table_sql = """
        CREATE TABLE IF NOT EXISTS emergency_type (
            emergency_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        # Create emergency type priority resource table if it doesn't exist
        create_emergency_type_priority_resource_table_sql = """
        CREATE TABLE IF NOT EXISTS emergency_type_priority_resource (
            emergency_type_priority_resource_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emergency_type_id INTEGER NOT NULL,
            priority_id INTEGER NOT NULL,
            recommended_resource_type_id INTEGER NOT NULL,
            recommended_quantity INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (emergency_type_id) REFERENCES emergency_type (emergency_type_id),
            FOREIGN KEY (priority_id) REFERENCES priority (priority_id),
            FOREIGN KEY (recommended_resource_type_id) REFERENCES resource_type (resource_type_id)
        );
        """

        conn.execute(create_priority_table_sql)
        print("Property table created or already exists.")

        conn.execute(create_resource_type_table_sql) 
        print("Resource type table created or already exists.")

        conn.execute(create_emergency_type_table_sql)
        print("Emergency type table created or already exists.")

        conn.execute(create_location_table_sql)
        print("Location table created or already exists.")

        conn.execute(create_emergency_type_priority_resource_table_sql)
        print("Emergency type priority resource table created or already exists.")

        conn.execute(create_resource_table_sql)
        print("Resource table created or already exists.")

        # conn.execute(create_incident_table_sql)
        # print("Incident table created or already exists.")

        # conn.execute(create_location_table_sql)
        # print("Location table created or already exists.")

        # conn.execute(create_resource_types_table_sql)
        # print("Resource types table created or already exists.")

  


        # Close the connection
        # conn.close()
        # print("Connection closed.")

        return conn
    except Error as e:
        print(e)

    return conn

