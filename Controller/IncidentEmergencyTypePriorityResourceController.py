
from sqlite3 import Error
from database import create_connection

def create_incident_emergency_type_priority_resource(incident_emergency_type_priority_resource):
    try:
        conn = create_connection('incident_management.db')
        sql = '''INSERT INTO incident_emergency_type_priority_resource(incident_id, emergency_type_priority_resource_id) VALUES(?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (incident_emergency_type_priority_resource.get_incident_id(), incident_emergency_type_priority_resource.get_emergency_type_priority_resource_id())) 
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created incident_emergency_type_priority_resource
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()

