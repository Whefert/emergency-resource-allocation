from sqlite3 import Error
from database import create_connection




def create_location(location):
    try:
        conn = create_connection('incident_management.db')
        
        # Check if the location already exists in the database
        sql_check = '''SELECT * FROM location WHERE location_id=?'''
        cur_check = conn.cursor()
        cur_check.execute(sql_check, (location.get_location_id(),))
        row = cur_check.fetchone()
        if row:
            return None  # Location already exists, return None or handle as needed

        
        
        sql = '''INSERT INTO location(location_id, zone, x_coordinate, y_coordinate) VALUES(?, ?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (location.get_location_id(), location.get_zone(), location.get_x_coordinate(), location.get_y_coordinate()))   
        conn.commit()
        # return cur.lastrowid  # Return the ID of the newly created location
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
       

def delete_location_in_db(location_id):
    try:
        conn = create_connection('incident_management.db')
        sql = '''DELETE FROM locations WHERE location_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (location_id,))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
       

def update_location_in_db(location):
    try:
        conn = create_connection('incident_management.db')
        sql = '''UPDATE location SET zone=?, x_coordinate=?, y_coordinate=? WHERE location_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (location.get_zone(), location.get_x_coordinate(), location.get_y_coordinate(), location.get_location_id()))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
       

def get_location_by_id(location_id):
    if location_id is None:
        return None

    try:
        conn = create_connection('incident_management.db')
        sql = '''SELECT * FROM location WHERE location_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (location_id,))
        row = cur.fetchone()
        return row
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
       

def get_all_locations():
    try:
        conn = create_connection('incident_management.db')
        sql = '''SELECT * FROM location'''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
       