from database import create_connection
from sqlite3 import Error

def create_incident_resource(incident_resource):
    try:
        conn = create_connection('incident_management.db')
        sql = '''INSERT INTO incident_resource( incident, resource) VALUES(?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (incident_resource.get_incident(), incident_resource.get_resource()))
        conn.commit()
        return cur.lastrowid  # Return the ID of the newly created incident resource
    except Error as e:
        print(e) 
    finally:
        # Close the connection
        conn.close()
      

def delete_incident_resource(incident, resource):
    try:
        conn = create_connection('incident_management.db')
        sql = '''DELETE FROM incident_resource WHERE incident=? AND resource=?'''
        cur = conn.cursor()
        cur.execute(sql, (incident, resource))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()


def reassign_incident_resource(incident_id, resource_id):
    try:
        conn = create_connection('incident_management.db')
        sql = '''UPDATE incident_resource SET resource=? WHERE incident=?'''
        cur = conn.cursor()
        cur.execute(sql, (resource_id, incident_id))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()


def get_all_incident_resources():
    try:
        conn = create_connection('incident_management.db')
        # Select incident and resource from the incident resource table 
        # Assuming the incident resource table is named 'incident_resource'
        sql = '''SELECT incident_resource.incident, incident_resource.resource 
                 FROM incident_resource 
                 LEFT JOIN incident ON incident_resource.incident = incident.incident_id
                 LEFT JOIN resource ON incident_resource.resource = resource.resource_id'''
    
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
      


def get_incident_resource_by_resouce_id(incident_resource_id):
    try:
        conn = create_connection('incident_management.db')
        sql = '''SELECT incident_resource.incident, incident_resource.resource 
                 FROM incident_resource 
                 WHERE incident_resource.incident_resource_id = ?'''
    
        cur = conn.cursor()
        cur.execute(sql, (incident_resource_id,))
        row = cur.fetchone()
        return row
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
      

# Get all the resources for a specific incident
# Assuming the incident_resource table has a foreign key relationship with the incident table
# and the resource table
def get_resources_by_incident_id(incident_id):
    try:
        conn = create_connection('incident_management.db')

        # Get the count of resources for each incident
    # sql = '''SELECT incident_resource.incident as incident_id,
    # COUNT(resource_type.resource_type_id) AS resource_count, resource_type.name
    # FROM incident_resource
    # LEFT JOIN resource ON incident_resource.resource = resource.resource_id
    # LEFT JOIN resource_type ON resource.resource_type_id = resource_type.resource_type_id
    # WHERE incident_resource.incident = ?
    # GROUP BY incident_resource.incident, resource_type.name'''



#     WITH tempTable AS (
# 	SELECT incident_resource.incident as incident_id, 
# 	incident_resource.resource, 
# 	resource.resource_type_id as rtid
# 	FROM incident_resource 
# 	LEFT JOIN 
# 	resource ON incident_resource.resource = resource.resource_id
# ) SELECT tempTable.incident_id, COUNT(resource_type.resource_type_id) AS resource_count, resource_type.name
# FROM resource_type
# LEFT JOIN tempTable ON tempTable.rtid = resource_type.resource_type_id
# GROUP BY tempTable.incident_id,
# resource_type.name


        sql = '''SELECT incident_resource.resource, resource.resource_type_id
                 FROM incident_resource 
                 LEFT JOIN resource ON incident_resource.resource = resource.resource_id
                 WHERE incident_resource.incident = ?        
                 '''
    
        cur = conn.cursor()
        cur.execute(sql, (incident_id,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
      


def get_resource_name_and_count_by_incident_id(incident_id):
    try:
        conn = create_connection('incident_management.db')
        sql = '''SELECT COUNT(resource_type.resource_type_id) AS resource_count, resource_type.name
        FROM incident_resource
     LEFT JOIN resource ON incident_resource.resource = resource.resource_id
     LEFT JOIN resource_type ON resource.resource_type_id = resource_type.resource_type_id
     WHERE incident_resource.incident = 1
     GROUP BY incident_resource.incident, resource_type.name'''
    
        cur = conn.cursor()
        cur.execute(sql, (incident_id,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
    finally:
        # Close the connection
        conn.close()
      