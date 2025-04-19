import sqlite3
from sqlite3 import Error
from database import create_connection


conn = create_connection('incident_management.db')

def create_location_in_db(location):
    try:
        sql = '''INSERT INTO locations(location_id, name, description) VALUES(?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (location.get_location_id(), location.get_name(), location.get_description()))
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created location
    except Error as e:
        print(e)

def delete_location_in_db(location_id):
    try:
        sql = '''DELETE FROM locations WHERE location_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (location_id,))
        conn.commit()
    except Error as e:
        print(e)

def update_location_in_db(location):
    try:
        sql = '''UPDATE locations SET name=?, description=? WHERE location_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (location.get_name(), location.get_description(), location.get_location_id()))
        conn.commit()
    except Error as e:
        print(e)

def get_location_by_id(location_id):
    try:
        sql = '''SELECT * FROM locations WHERE location_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (location_id,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    return None

def get_all_locations():
    try:
        sql = '''SELECT * FROM locations'''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    return None