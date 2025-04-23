from database import create_connection
from sqlite3 import Error


def create_incident_in_db(incident):
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
