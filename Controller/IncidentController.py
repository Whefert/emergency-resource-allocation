from database import create_connection
from sqlite3 import Error


def create_incident(incident):
    try:
        conn = create_connection('incident_management.db')
        sql = '''INSERT INTO incident(incident_id, location, description) VALUES(?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (incident.get_incident_id(), incident.get_location(), incident.get_description()))
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created incident
    except Error as e:
        print(e) 
    finally:
        # Close the connection
        conn.close()
        print("Connection closed.")

def get_all_incidents():
    try:
        conn = create_connection('incident_management.db')
        # Select incident and resource from the incident resource table 
        # Assuming the incident resource table is named 'incident_resource'
        sql = '''SELECT incident.incident_id, incident.location, incident.description, incident.status, incident_resource.resources 
                 FROM incident 
                 LEFT JOIN incident_resource ON incident.incident_id = incident_resource.incident_id
                 JOIN resource ON incident_resource.resource_id = resource.resource_id'''
    
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