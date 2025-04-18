import sqlite3
from sqlite3 import Error
import inquirer

class Incident:
    def __init__(self, description, priority, status,incident_id = None, required_resources=None, assigned_resources=None):
        self.incident_id = incident_id # This will be auto-incremented by the database
        self.priority = priority
        self.required_resources = required_resources if required_resources is not None else []
        self.assigned_resources = assigned_resources if assigned_resources is not None else []
        self.description = description
        self.status = status

    @staticmethod
    def prompt_incident_data(conn):
        # Get all locations from the database

        questions = [
            inquirer.Text('description', message="Enter incident description"),
            inquirer.List("location", message="Select incident location", choices=['Location1', 'Location2', 'Location3']),       
            inquirer.List('priority', message="Select incident priority", choices=['Low', 'Medium', 'High']),
            inquirer.List('status', message="Select incident status", choices=['Open', 'In Progress', 'Resolved'])
        ]
        answers = inquirer.prompt(questions)
        # Create a new incident object with the provided data
        incident = Incident(
            incident_id=None,  # This will be auto-incremented by the database
            description=answers['description'],
            priority=answers['priority'],
            status=answers['status']
        )
        # Insert the incident into the database and get the incident ID
        incident.set_incident_id(incident.create_incident(conn))
        print(f"Incident created with ID: {incident.get_incident_id()}")

    def create_incident(self, conn):
        try:
            sql = '''INSERT INTO incidents(incident_id, description, priority, status) VALUES(?, ?, ?, ?)'''
            cur = conn.cursor()
            cur.execute(sql, (self.incident_id, self.description, self.priority, self.status))
            conn.commit()
            return cur.lastrowid  # Return the ID of the newly created incident
        except Error as e:
            print(e)    

    # setters and getters for the incident attributes
    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
    
    def set_priority(self, priority):
        self.priority = priority
    def get_priority(self):
        return self.priority
    
    def set_status(self, status):
        self.status = status
    def get_status(self):
        return self.status
    
    def set_incident_id(self, incident_id):
        self.incident_id = incident_id
    def get_incident_id(self):
        return self.incident_id
    
    def set_required_resources(self, required_resources):
        self.required_resources = required_resources
    def get_required_resources(self):
        return self.required_resources


    def __repr__(self):
        return f"Incident({self.incident_id}, {self.description}, {self.status})"