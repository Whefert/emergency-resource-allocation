from database import create_connection
from sqlite3 import Error


def create_status(status):
    try:
        conn = create_connection('incident_management.db')
        sql = '''INSERT INTO status(status_id, name, description) VALUES(?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (status.get_status_id(), status.get_name(), status.get_description()))
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created status
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        print("Connection closed.")



def get_all_statuses():
    try:
        conn = create_connection('incident_management.db')
        sql = '''SELECT * FROM status'''
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