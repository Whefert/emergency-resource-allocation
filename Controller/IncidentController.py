from database import create_connection
from sqlite3 import Error



def create_incident(incident):
    try:
        conn = create_connection('incident_management.db')
        sql = '''INSERT INTO incident(incident_id, location, description, status) VALUES(?, ?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (incident.get_incident_id(), incident.get_location(), incident.get_description(), incident.get_status()))
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created incident
    except Error as e:
        print(e) 
    finally:
        # Close the connection
        conn.close()

def get_all_incidents():
    try:
        conn = create_connection('incident_management.db')
        # Select incident from the incident table and join with the status table and location table

        sql = '''SELECT incident.incident_id, incident.location, incident.description, incident.status 
                FROM incident'''

        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
