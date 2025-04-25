from database import create_connection
from sqlite3 import Error


def create_resource(resource):
    try:
        conn = create_connection('incident_management.db')  
        # Check if the resource already exists in the database
        sql_check = '''SELECT * FROM resource WHERE resource_id=? AND resource_type_id=?'''
        cur_check = conn.cursor()
        cur_check.execute(sql_check, (resource.get_resource_id(), resource.get_resource_type_id()))
        row = cur_check.fetchone()
        if row:
            return None # Resource already exists, return None or handle as needed

        sql = '''INSERT INTO resource(resource_id,resource_type_id) VALUES(?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (resource.get_resource_id(), resource.get_resource_type_id()))   
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created resource type
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        