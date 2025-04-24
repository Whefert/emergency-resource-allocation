import sqlite3  
from sqlite3 import Error
from database import create_connection




def create_emergency_type(emergency_type):
    conn = create_connection('incident_management.db')
    try:
        # Check if the emergency type already exists
        sql_check = '''SELECT * FROM emergency_type WHERE emergency_type_id = ?'''
        cur = conn.cursor()
        cur.execute(sql_check, (emergency_type.get_emergency_type_id(),))
        row = cur.fetchone()
        if row:
            print("Emergency type already exists.")
            return None
        # If it doesn't exist, insert the new emergency type

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

def get_all_emergency_types():
    try:
        conn = create_connection('incident_management.db')
        sql = '''SELECT * FROM emergency_type'''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()