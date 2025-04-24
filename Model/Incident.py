import inquirer
from Controller.IncidentController import create_incident, get_all_incidents
from Controller.LocationController import get_all_locations, get_location_by_id
from Controller.PriorityController import get_all_priorities
from Controller.StatusController import get_all_statuses, get_status_by_id
from Controller.IncidentResourceController import get_resources_by_incident_id
from Controller.EmergencyTypeController import get_all_emergency_types  
from Model.Resource import Resource
from Controller.IncidentEmergencyTypePriorityResourceController import create_incident_emergency_type_priority_resource
from Model.IncidentEmergencyTypePriorityResource import IncidentEmergencyTypePriorityResource
from Controller.EmergencyTypePriorityResourceController import get_emergency_type_priority_resource_by_priority_and_emergency_type

class Incident:
    def __init__(self, location:int, description:str, status:int, incident_id:int=None):
        self.status = status
        self.incident_id = incident_id # This will be auto-incremented by the database
        self.location = location
        self.description = description
        self.resources = []  # This will hold the resources associated with the incident
        self.emergency_type = None  # This will hold the emergency type associated with the incident
        self.priority = None  # This will hold the priority associated with the incident

    @staticmethod
    def prompt_incident_data():
        questions = [
        # Create a list of tuples for inquirer
            inquirer.List("location", message="Select incident location", choices=[(loc[1], loc[0]) for loc in get_all_locations()]),       
            inquirer.Text('description', message="Enter incident description"),
            inquirer.List('priority', message="Select incident priority", choices=[(pr[2], pr[0]) for pr in get_all_priorities()]),
            inquirer.List('status', message="Select incident status", choices=[(st[1], st[0]) for st in get_all_statuses()]),   
            inquirer.List ('emergency_type', message="Select incident emergency type", choices=[(et[1], et[0]) for et in get_all_emergency_types()]),
     ]   
        answers = inquirer.prompt(questions)
        # Create the incident in the database
        incident_id = create_incident(Incident(
            location=answers['location'],
            description=answers['description'], 
            status=answers['status']
        ))

        # FInd the incident emergency type and priority in the database
        emergency_type = answers['emergency_type']
        priority = answers['priority']

        # Get the emergency type and priority from the database using the IDs
        required_resources = get_emergency_type_priority_resource_by_priority_and_emergency_type(priority, emergency_type)
        
        # loop through the required resources and assign them to the incident in the incident_resources table

  
     
        # Create the incident emergency type and priority in the database

    @staticmethod
    def show_all_incidents():
        # Get all incidents from the database and create Incident objects
        incidents = [ Incident(location=incident[1], description=incident[2], status=incident[3], incident_id=incident[0]) for incident in get_all_incidents() ]
        # Print the incidents        
        if incidents:
            print("Incidents:")
            for incident in incidents:
                print(incident)
        else:
            print("No incidents found.")

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
        # Get the status name from the database using the status ID
        status_name = get_status_by_id(self.get_status())[1] if self.get_status() else "Unknown"
        location_zone = get_location_by_id(self.get_location())[1] if self.get_location() else "Unknown"
        incident_resources = get_resources_by_incident_id(self.get_incident_id()) if self.get_incident_id() else []
        # Create Resource objects from the incident resources and set them to the incident
        self.set_resources([Resource(resource[1], resource[0]) for resource in incident_resources] if incident_resources else [])

        return f"Incident ID: {self.incident_id}, Location: {location_zone}, Description: {self.description}, Status: {status_name}\n Resources: {', '.join([str(resource) for resource in self.get_resources()]) if self.get_resources() else 'No resources assigned'}"

        # Representation of the object for debugging
    def __repr__(self):
        return f"Incident(incident_id={self.incident_id}, location={self.location}, description={self.description}, status={self.status})"