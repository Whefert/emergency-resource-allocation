import sqlite3
from sqlite3 import Error
from database import create_connection
from Model.EmergencyTypePriorityResource import EmergencyTypePriorityResource

def create_emergency_type_priority_resource(emergency_type_priority_resource: EmergencyTypePriorityResource):

    conn = create_connection('incident_management.db')
    try:
        sql = '''INSERT INTO emergency_type_priority_resource(emergency_type_id, priority_id, recommended_resource_type_id, recommended_quantity) VALUES(?, ?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (emergency_type_priority_resource.get_emergency_type_id(), emergency_type_priority_resource.get_priority_id(), emergency_type_priority_resource.get_recommended_resource_type_id(), emergency_type_priority_resource.get_recommended_quantity()))
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created emergency type priority resource
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        print("Connection closed.")