from database import create_connection
from sqlite3 import Error


def create_status(status):
    try:
        conn = create_connection('incident_management.db')

        # Check if the status already exists in the database
        sql_check = '''SELECT * FROM status WHERE status_id=?'''
        cur_check = conn.cursor()
        cur_check.execute(sql_check, (status.get_status_id(),))
        row = cur_check.fetchone()
        if row:
            return None # Status already exists, return None or handle as needed

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
        


def get_status_by_id(status_id):
    try:
        conn = create_connection('incident_management.db')
        sql = '''SELECT * FROM status WHERE status_id = ?'''
        cur = conn.cursor()
        cur.execute(sql, (status_id,))
        row = cur.fetchone()
        return row
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        