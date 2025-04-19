from database import create_connection
import sqlite3
from sqlite3 import Error

conn = create_connection('incident_management.db')

def create_resource_type_in_db(resource_type):
    try:
        sql = '''INSERT INTO resource_types(resource_type_id, name, description) VALUES(?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (resource_type.get_resource_type_id(), resource_type.get_name(), resource_type.get_description()))
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created resource type
    except Error as e:
        print(e)

def delete_resource_type_in_db(resource_type_id):
    try:
        sql = '''DELETE FROM resource_types WHERE resource_type_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (resource_type_id,))
        conn.commit()
    except Error as e:
        print(e)

def update_resource_type_in_db(resource_type):
    try:
        sql = '''UPDATE resource_types SET name=?, description=? WHERE resource_type_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (resource_type.get_name(), resource_type.get_description(), resource_type.get_resource_type_id()))
        conn.commit()
    except Error as e:
        print(e)

def get_resource_type_by_id(resource_type_id):
    try:
        sql = '''SELECT * FROM resource_types WHERE resource_type_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (resource_type_id,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    return None 

def get_all_resource_types():
    try:
        sql = '''SELECT * FROM resource_types'''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    return None

