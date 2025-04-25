from database import create_connection
from sqlite3 import Error



def create_incident(incident):
    try:
        conn = create_connection('incident_management.db')

        # Check if the incident already exists in the database
        sql_check = '''SELECT * FROM incident WHERE incident_id=?'''
        cur_check = conn.cursor()
        cur_check.execute(sql_check, (incident.get_incident_id(),))
        row = cur_check.fetchone()
        if row:
            return None
        # Incident already exists, return None or handle as needed

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


def update_incident_location(incident_id:int, new_location:str):
    try:
        conn = create_connection('incident_management.db')
        sql = '''UPDATE incident SET location=? WHERE incident_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (new_location, incident_id))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()

def update_incident_description(incident_id:int, new_description:str):
    try:
        conn = create_connection('incident_management.db')
        sql = '''UPDATE incident SET description=? WHERE incident_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (new_description, incident_id))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()

def update_incident_status(incident_id:int, new_status:str):
    try:
        conn = create_connection('incident_management.db')
        sql = '''UPDATE incident SET status=? WHERE incident_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (new_status, incident_id))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()

