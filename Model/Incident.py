import sqlite3
from sqlite3 import Error
import inquirer
from Controller.IncidentController import create_incident_in_db

class Incident:
    def __init__(self, incident_id, location, description):
        self.incident_id = incident_id # This will be auto-incremented by the database
        self.location = location
        self.description = description

    @staticmethod
    def prompt_incident_data():
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
        incident.set_incident_id(create_incident_in_db(incident))
        print(f"Incident created with ID: {incident.get_incident_id()}")

   
    # Getters and Setters

    def get_incident_id(self):
        return self.incident_id
    
    def get_location(self):
        return self.location
    
    def get_description(self):
        return self.description
    
    def set_incident_id(self, incident_id):
        self.incident_id = incident_id

    def set_location(self, location):
        self.location = location
    
    def set_description(self, description):
        self.description = description

    # String representation of the object
    def __str__(self):
        return f"Incident(id={self.incident_id}, location={self.location}, description={self.description})"
    
    # Representation of the object for debugging
    def __repr__(self):
        return f"Incident(incident_id={self.incident_id}, location={self.location}, description={self.description})"