from sqlite3 import Error
from database import create_connection



def create_priority(priority):
    conn = create_connection('incident_management.db')  
    try:
        # Check if the priority already exists
        sql_check = '''SELECT * FROM priority WHERE priority_id = ?'''
        cur = conn.cursor()
        cur.execute(sql_check, (priority.get_priority_id(),))
        row = cur.fetchone()
        if row:
            return None  # Priority already exists, return None

        sql = '''INSERT INTO priority(priority_id, name, description) VALUES(?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (priority.get_priority_id(), priority.get_name(), priority.get_description()))
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created priority
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        


def get_all_priorities():
    try:
        conn = create_connection('incident_management.db')
        sql = '''SELECT * FROM priority'''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
        