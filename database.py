import sqlite3
from sqlite3 import Error
from datetime import datetime
import csv


# Delete the database file if it exists
def drop_tables(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS incident")
    cursor.execute("DROP TABLE IF EXISTS location")
    cursor.execute("DROP TABLE IF EXISTS resource")
    cursor.execute("DROP TABLE IF EXISTS resource_type")
    cursor.execute("DROP TABLE IF EXISTS priority")
    cursor.execute("DROP TABLE IF EXISTS emergency_type")
    cursor.execute("DROP TABLE IF EXISTS emergency_type_priority_resource")
    cursor.execute("DROP TABLE IF EXISTS incident_emergency_type_priority_resource")
    cursor.execute("DROP TABLE IF EXISTS incident_resource")
    cursor.execute("DROP TABLE IF EXISTS status")
    conn.commit()
    conn.close()




# TODO: Create a function to create the database separate from create the connec


def create_connection(db_name):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        # Create incident table if it doesn't exist
        create_incident_table_sql = """
        CREATE TABLE IF NOT EXISTS incident (
            incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
            location INTEGER NOT NULL,
            description TEXT NOT NULL,
            status INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (location) REFERENCES location (location_id),
            FOREIGN KEY (status) REFERENCES status (status_id)
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
            emergency_type_id INTEGER NOT NULL,
            priority_id INTEGER NOT NULL,
            resource_type_id INTEGER NOT NULL,
            recommended_quantity INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (emergency_type_id) REFERENCES emergency_type (emergency_type_id),
            FOREIGN KEY (priority_id) REFERENCES priority (priority_id),
            FOREIGN KEY (resource_type_id) REFERENCES resource_type (resource_type_id)
            PRIMARY KEY (emergency_type_id, priority_id, resource_type_id)
        );
        """

        # Create incident emergency type priority resource table if it doesn't exist
        create_incident_emergency_type_priority_resource_table_sql = """
        CREATE TABLE IF NOT EXISTS incident_emergency_type_priority_resource (
            incident_id INTEGER NOT NULL ,
            emergency_type_priority_resource_id INTEGER KEY NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (incident_id) REFERENCES incidents (incident_id),
            FOREIGN KEY (emergency_type_priority_resource_id) REFERENCES emergency_type_priority_resource (emergency_type_priority_resource_id)
            PRIMARY KEY (incident_id, emergency_type_priority_resource_id)
        );
        """

        # Creae incident resource table if it doesn't exist
        create_incident_resource_table_sql = """
        CREATE TABLE IF NOT EXISTS incident_resource (
            incident INTEGER NOT NULL,
            resource INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (incident) REFERENCES incident (incident_id),
            FOREIGN KEY (resource) REFERENCES resource (resource_id)
            PRIMARY KEY (incident, resource)
        );
        """

        # Create status table if it doesn't exist
        create_status_table_sql = """
        CREATE TABLE IF NOT EXISTS status (
            status_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        conn.execute(create_incident_table_sql)
        conn.execute(create_priority_table_sql)
        conn.execute(create_resource_type_table_sql) 
        conn.execute(create_location_table_sql)
        conn.execute(create_resource_table_sql)
        conn.execute(create_emergency_type_priority_resource_table_sql)
        conn.execute(create_status_table_sql)
        conn.execute(create_emergency_type_table_sql)
        conn.execute(create_incident_emergency_type_priority_resource_table_sql)
        conn.execute(create_incident_resource_table_sql)
    
        return conn
    except Error as e:
        print(e)

    return conn

