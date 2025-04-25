
from sqlite3 import Error
from database import create_connection

def create_incident_emergency_type_priority_resource(incident_emergency_type_priority_resource):
    try:
        conn = create_connection('incident_management.db')
        # Check if the incident_emergency_type_priority_resource already exists in the database
        sql_check = '''SELECT * FROM incident_emergency_type_priority_resource WHERE incident_id=? AND emergency_type_priority_resource_id=?'''
        cur_check = conn.cursor()
        cur_check.execute(sql_check, (incident_emergency_type_priority_resource.get_incident_id(), incident_emergency_type_priority_resource.get_emergency_type_priority_resource_id()))
        row = cur_check.fetchone()
        if row:
            return None # incident_emergency_type_priority_resource already exists, return None or handle as needed


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


def update_incident_emergency_type_priority_resource(incident_id, emergency_type_priority_resource_id):
    try:
        conn = create_connection('incident_management.db')
        sql = '''UPDATE incident_emergency_type_priority_resource SET emergency_type_priority_resource_id=? WHERE incident_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (emergency_type_priority_resource_id, incident_id))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()


def get_incident_emergency_type_priority_resource_by_incident_id(incident_id):
    try:
        conn = create_connection('incident_management.db')
        # Get the incident_emergency_type_priority_resource left join emergency_type_priority_resource table
        sql = '''SELECT incident_emergency_type_priority_resource.incident_id, 
        incident_emergency_type_priority_resource.emergency_type_priority_resource_id, 
        emergency_type_priority_resource.resource_type_id, 
        emergency_type_priority_resource.recommended_quantity FROM incident_emergency_type_priority_resource 
        LEFT JOIN emergency_type_priority_resource 
        ON incident_emergency_type_priority_resource.emergency_type_priority_resource_id = emergency_type_priority_resource.id 
        WHERE incident_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (incident_id,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()