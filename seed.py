import csv
from sqlite3 import Error
from Controller.ResourceTypeController import create_resource_type_in_db, delete_resource_type_in_db, update_resource_type_in_db, get_resource_type_by_id, get_all_resource_types
from Model.ResourceType import ResourceType
from Model.EmergencyType import EmergencyType
from Controller.EmergencyTypeController import create_emergency_type
from Model.Priority import Priority
from Controller.PriorityController import create_priority
from Model.Location import Location
from Controller.LocationController import create_location
from Model.EmergencyTypePriorityResource import EmergencyTypePriorityResource
from Controller.EmergencyTypePriorityResourceController import create_emergency_type_priority_resource
from Controller.ResourceController import create_resource
from Model.Resource import Resource
from Controller.IncidentEmergencyTypePriorityResourceController import create_incident_emergency_type_priority_resource
from Model.IncidentEmergencyTypePriorityResource import IncidentEmergencyTypePriorityResource
from Controller.IncidentController import create_incident
from Model.Incident import Incident
from Controller.StatusController import create_status
from Model.Status import Status


def seed_resource_types():
    # Raead the CSV file in the data folder and insert data into the resource_types table
    # Assuming the CSV file has columns: name, description

    try:
        with open('./data/resource_type.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                resource_type_id, name, description = row
                resource_type = ResourceType( name, description, resource_type_id)
                #TODO: Check if the resource type already exists in the database
                create_resource_type_in_db(resource_type)
                print("Resource types seeded successfully.")
    except Error as e:
        print(e)


def seed_priority():
    # Read the CSV file in the data folder and insert data into the priority table
    # Assuming the CSV file has columns: name, description

    try:
        with open('./data/priority.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                priority_id, name, description = row
                priority = Priority(name, description, priority_id)
                create_priority(priority)
                print("Priority seeded successfully.")
    except Error as e:
        print(e)

def seed_emergency_type():
    # Read the CSV file in the data folder and insert data into the emergency_types table
    # Assuming the CSV file has columns: name, description

    try:
        with open('./data/emergency_type.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                emergency_type_id, name, description = row
                print(emergency_type_id, name, description)
                emergency_type = EmergencyType(name, description, emergency_type_id)
                create_emergency_type(emergency_type)
                print("Emergency types seeded successfully.")
    except Error as e:
        print(e)

def seed_location():
    # Read the CSV file in the data folder and insert data into the locations table
    # Assuming the CSV file has columns: name, description

    try:
        with open('./data/location.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                location_id, zone, x_coordinate, y_coordinate = row
                location = Location(zone, x_coordinate, y_coordinate, location_id)
                print(location)
                create_location(location)
                print("Location seeded successfully.")
    except Error as e:
        print(e)

def seed_emergency_type_priority_resource():
    # Read the CSV file in the data folder and insert data into the emergency_type_priority_resource table
    # Assuming the CSV file has columns: name, description
    try:
        with open('./data/emergency_type_priority_resource.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                emergency_type_priority_resource_id, emergency_type_id, priority_id, recommended_resource_type_id, recommended_quantity = row
                emergency_type_priority_resource = EmergencyTypePriorityResource(emergency_type_id, priority_id, recommended_resource_type_id, recommended_quantity, emergency_type_priority_resource_id)
                create_emergency_type_priority_resource(emergency_type_priority_resource)
                print("Emergency type priority resource seeded successfully.")
    except Error as e:
        print(e)
    
def seed_resource():
    # Read the CSV file in the data folder and insert data into the resources table
    # Assuming the CSV file has columns: name, description
    try:
        with open('./data/resource.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                resource_id, resource_type_id = row
                resource = Resource(resource_type_id, resource_id)
                print(resource)
                create_resource(resource)
                print("Resource seeded successfully.")
    except Error as e:
        print(e)

def seed_incident_emergency_type_priority_resource():
    # Read the CSV file in the data folder and insert data into the incident_emergency_type_priority_resource table
    # Assuming the CSV file has columns: name, description
    try:
        with open('./data/incident_emergency_type_priority_resource.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                incident_emergency_type_priority_resource_id, incident_id, emergency_type_priority_resource_id = row
                incident_emergency_type_priority_resource = IncidentEmergencyTypePriorityResource(incident_id, emergency_type_priority_resource_id, incident_emergency_type_priority_resource_id)
                create_incident_emergency_type_priority_resource(incident_emergency_type_priority_resource)
                print("Incident emergency type priority resource seeded successfully.")
    except Error as e:
        print(e)

def seed_incident():
    try:
        with open('./data/incident.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                incident_id, location, description, status = row
                incident = Incident(incident_id, location, description, status)
                create_incident(incident)
                print("Incident seeded successfully.")
    except Error as e:
        print(e)

def seed_status():
    # Read the CSV file in the data folder and insert data into the status table
    # Assuming the CSV file has columns: name, description
    try:
        with open('./data/status.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                status_id, name, description = row
                status = Status(name, description, status_id)
                create_status(status)
                print("Status seeded successfully.")
    except Error as e:
        print(e)


def seed_db():
    # Seed the database with initial data
    seed_resource_types()
    seed_priority()
    seed_emergency_type()
    seed_location()
    seed_emergency_type_priority_resource()
    seed_resource()
    seed_incident_emergency_type_priority_resource()
    seed_incident()
    seed_status()