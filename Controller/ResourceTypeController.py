from database import create_connection
from sqlite3 import Error



def create_resource_type_in_db(resource_type):
    conn = create_connection('incident_management.db')
    try:
        sql = '''INSERT INTO resource_type(resource_type_id, name, description) VALUES(?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (resource_type.get_resource_type_id(), resource_type.get_name(), resource_type.get_description()))
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created resource type
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        print("Connection closed.")

def delete_resource_type_in_db(resource_type_id):
    conn = create_connection('incident_management.db')
    try:
        sql = '''DELETE FROM resource_types WHERE resource_type_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (resource_type_id,))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        print("Connection closed.")
        

def update_resource_type_in_db(resource_type):
    conn = create_connection('incident_management.db')
    try:
        sql = '''UPDATE resource_types SET name=?, description=? WHERE resource_type_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (resource_type.get_name(), resource_type.get_description(), resource_type.get_resource_type_id()))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        print("Connection closed.")

def get_resource_type_by_id(resource_type_id):
    conn = create_connection('incident_management.db')
    try:
        sql = '''SELECT * FROM resource_types WHERE resource_type_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (resource_type_id,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        print("Connection closed.")

def get_all_resource_types():
    conn = create_connection('incident_management.db')
    try:
        sql = '''SELECT * FROM resource_types'''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        print("Connection closed.")

