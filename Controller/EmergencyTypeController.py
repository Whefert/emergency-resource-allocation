import sqlite3  
from sqlite3 import Error
from database import create_connection




def create_emergency_type(emergency_type):
    conn = create_connection('incident_management.db')
    try:
        sql = '''INSERT INTO emergency_type(emergency_type_id, name, description) VALUES(?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (emergency_type.get_emergency_type_id(), emergency_type.get_name(), emergency_type.get_description()))
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created emergency type
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        print("Connection closed.")