import inquirer
from Controller.IncidentController import create_incident
from Controller.LocationController import get_all_locations
from Controller.PriorityController import get_all_priorities
from Controller.StatusController import get_all_statuses

class Incident:
    def __init__(self, location:int, description:str, status:int, incident_id:int=None):
        self.status = status
        self.incident_id = incident_id # This will be auto-incremented by the database
        self.location = location
        self.description = description
        self.resources = []  # This will hold the resources associated with the incident

    @staticmethod
    def prompt_incident_data():
        questions = [
        # Create a list of tuples for inquirer
            inquirer.List("location", message="Select incident location", choices=[(loc[1], loc[0]) for loc in get_all_locations()]),       
            inquirer.Text('description', message="Enter incident description"),
            inquirer.List('priority', message="Select incident priority", choices=[(pr[2], pr[0]) for pr in get_all_priorities()]),
            inquirer.List('status', message="Select incident status", choices=[(st[1], st[0]) for st in get_all_statuses()]),   ]
        answers = inquirer.prompt(questions)
        # Create the incident in the database
        create_incident(Incident(
            location=answers['location'],
            description=answers['description'], 
            status=answers['status']
        ))

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

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
    
    def set_resources(self, resources):
        self.resources = resources

    def get_resources(self):
        return self.resources

    # String representation of the object
    def __str__(self):
        return f"Incident(incident_id={self.incident_id}, location={self.location}, description={self.description}, status={self.status})"    
    # Representation of the object for debugging
    def __repr__(self):
        return f"Incident(incident_id={self.incident_id}, location={self.location}, description={self.description}, status={self.status})"