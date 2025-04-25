import sqlite3
from sqlite3 import Error
from database import create_connection
from Model.EmergencyTypePriorityResource import EmergencyTypePriorityResource

def create_emergency_type_priority_resource(emergency_type_priority_resource: EmergencyTypePriorityResource):

    try:
        conn = create_connection('incident_management.db')  

        # Check if the emergency type priority resource already exists in the database
        sql_check = '''SELECT * FROM emergency_type_priority_resource WHERE emergency_type_id=? AND priority_id=? AND resource_type_id=?'''
        cur_check = conn.cursor()
        cur_check.execute(sql_check, (emergency_type_priority_resource.get_emergency_type_id(), emergency_type_priority_resource.get_priority_id(), emergency_type_priority_resource.get_resource_type_id()))
        row = cur_check.fetchone()
        if row:
            return None # Emergency type priority resource already exists, return None or handle as needed

        sql = '''INSERT INTO emergency_type_priority_resource(emergency_type_id, priority_id, resource_type_id, recommended_quantity) VALUES(?, ?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (emergency_type_priority_resource.get_emergency_type_id(), emergency_type_priority_resource.get_priority_id(), emergency_type_priority_resource.get_resource_type_id(), emergency_type_priority_resource.get_recommended_quantity()))
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created emergency type priority resource
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
  
def get_emergency_type_priority_resource_by_priority_and_emergency_type(priority_id, emergency_type_id):
    conn = create_connection('incident_management.db')
    try:
        sql = '''SELECT emergency_type_priority_resource.resource_type_id, emergency_type_priority_resource.recommended_quantity FROM emergency_type_priority_resource WHERE priority_id=? AND emergency_type_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (priority_id, emergency_type_id))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()

