import sqlite3
from sqlite3 import Error
from functions import create_connection

conn = create_connection('incident_management.db')

def create_incident_in_db(incident):
    try:
        sql = '''INSERT INTO incidents(incident_id, description, priority, status) VALUES(?, ?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (incident.get_incident_id(), incident.get_description(), incident.get_priority(), incident.get_status()))
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created incident
    except Error as e:
        print(e) 

def delete_incident_in_db(incident_id):
    try:
        sql = '''DELETE FROM incidents WHERE incident_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (incident_id,))
        conn.commit()
    except Error as e:
        print(e)

def update_incident_in_db(incident):
    try:
        sql = '''UPDATE incidents SET description=?, priority=?, status=? WHERE incident_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (incident.get_description(), incident.get_priority(), incident.get_status(), incident.get_incident_id()))
        conn.commit()
    except Error as e:
        print(e)

def get_incident_by_id(incident_id):
    try:
        sql = '''SELECT * FROM incidents WHERE incident_id=?'''
        cur = conn.cursor()
        cur.execute(sql, (incident_id,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    return None

def get_all_incidents():
    try:
        sql = '''SELECT * FROM incidents'''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    return None