from database import create_connection
from sqlite3 import Error


def create_resource(resource):
    conn = create_connection('incident_management.db')
    try:
        sql = '''INSERT INTO resource(resource_id,resource_type_id) VALUES(?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, resource.get_resource_id(), resource.get_resource_type_id())   
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created resource type
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        print("Connection closed.")