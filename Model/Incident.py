import inquirer
from Controller.IncidentController import create_incident, get_all_incidents, update_incident_location, update_incident_description, update_incident_status
from Controller.LocationController import get_all_locations, get_location_by_id
from Controller.PriorityController import get_all_priorities
from Controller.StatusController import get_all_statuses, get_status_by_id
from Controller.IncidentResourceController import get_resources_by_incident_id, get_available_resources_by_type, get_all_available_resources, add_resource_to_incident, remove_resource_from_incident
from Controller.EmergencyTypeController import get_all_emergency_types  
from Model.Resource import Resource
from Controller.ResourceTypeController import get_all_resource_types
from Controller.IncidentEmergencyTypePriorityResourceController import update_incident_emergency_type_priority_resource, get_incident_emergency_type_priority_resource_by_incident_id
from Model.IncidentEmergencyTypePriorityResource import IncidentEmergencyTypePriorityResource
from Controller.EmergencyTypePriorityResourceController import get_emergency_type_priority_resource_by_priority_and_emergency_type
from Model.EmergencyTypePriorityResource import EmergencyTypePriorityResource

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

        # TODOD: Create the incident emergency type priority resource in the database
  

        # Find the incident emergency type and priority in the database
        emergency_type = answers['emergency_type']
        priority = answers['priority']

        # Get the emergency type and priority from the database using the IDs
        required_resources = get_emergency_type_priority_resource_by_priority_and_emergency_type(priority, emergency_type)
        for resource_id, recommended_quantity in required_resources:
            # Find resource not assigned to an incident in the incident_resources table
            available_resources = get_available_resources_by_type(resource_id)
            if available_resources:
                #Check if the available resources are greater than or equal to the recommended quantity
                if len(available_resources) >= recommended_quantity:
                     for i in range(recommended_quantity):
                        # Assign the resource to the incident in the incident_resources table
                        add_resource_to_incident(incident_id, available_resources[i][0])              
                else:
                    # If not enough resources are available, assign all available resources to the incident
                    for i in range(len(available_resources)):
                        add_resource_to_incident(incident_id, available_resources[i][0])
            
        # loop through the required resources and assign them to the incident in the incident_resources table
        print(f"Required resources for incident {incident_id}:")


    @staticmethod
    def update_incident_location(incident_id:int):
        # Get all locations from the database and create a list of tuples for inquirer
        questions = [
            inquirer.List("location", message="Select new incident location", choices= [(loc[1], loc[0]) for loc in get_all_locations()]),
        ]
        answers = inquirer.prompt(questions)
        # Update the incident location in the database
        update_incident_location(incident_id, answers['location'])
    
    @staticmethod
    def update_incident_description(incident_id:int):
        # Get the new description from the user
        questions = [
            inquirer.Text('description', message="Enter new incident description"),
        ]
        answers = inquirer.prompt(questions)
        # Update the incident description in the database
        update_incident_description(incident_id, answers['description'])

    @staticmethod
    def update_incident_status(incident_id:int):
        # Get all statuses from the database and create a list of tuples for inquirer
        questions = [
            inquirer.List("status", message="Select new incident status", choices=[(st[1], st[0]) for st in get_all_statuses()]),
        ]
        answers = inquirer.prompt(questions)
        # Update the incident status in the database
        update_incident_status(incident_id, answers['status'])

    @staticmethod
    def update_incident_resources(incident_id:int):
        # Get all resources from the database and create a list of tuples for inquirer
        questions = [
            # Ask if the user wants to add or remove a resource
            inquirer.List("action", message="Do you want to add or remove a resource?", choices=["Add", "Remove"]),
            # Confirm what kind of resource the user wants to add
            # If the user wants to add a resource, show the available resources
            inquirer.List("addResource", message="Select resource to add", choices=[(str(res[2]), res[0]) for res in get_all_available_resources()],
                            ignore=lambda answers: answers['action'] == 'Remove'
                            ),
            # If the user wants to remove a resource, show the resources assigned to the incident
            inquirer.List("removeResource", message="Select resource to remove", choices=[(str(res[2]), res[0]) for res in get_resources_by_incident_id(incident_id)],
                            ignore=lambda answers: answers['action'] == 'Add'
                            )
        ]
        answers = inquirer.prompt(questions)
        # If the user wants to add a resource, add it to the incident in the database
        if answers['action'] == 'Add':
            add_resource_to_incident(incident_id, answers['addResource'])
        # If the user wants to remove a resource, remove it from the incident in the database
        elif answers['action'] == 'Remove':
            # Remove the resource from the incident in the database
            remove_resource_from_incident(incident_id, answers['removeResource'])

    @staticmethod
    def update_incident_priority(incident_id:int):
        # Get all priorities from the database and create a list of tuples for inquirer
        questions = [
            inquirer.List("priority", message="Select new incident priority", choices=[(pr[2], pr[0]) for pr in get_all_priorities()]),
        ]
        answers = inquirer.prompt(questions)
        
        # Find the incident emergency type and priority in the database

        # Find the emergency type priority resource in the database using the priority ID


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

        return (
            f"Incident {self.incident_id}: Location: {location_zone}, Description: {self.description}, Status: {status_name}\n"
            f"Resources: {', '.join([str(resource) for resource in self.get_resources()]) if self.get_resources() else 'No resources assigned'}"
        )
    
        # Representation of the object for debugging
    def __repr__(self):
        return f"Incident(incident_id={self.incident_id}, location={self.location}, description={self.description}, status={self.status})"