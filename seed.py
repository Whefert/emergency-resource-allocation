from database import create_connection
import csv
import sqlite3
from sqlite3 import Error
import os
from Controller.ResourceTypeController import create_resource_type_in_db, delete_resource_type_in_db, update_resource_type_in_db, get_resource_type_by_id, get_all_resource_types
from Model.ResourceType import ResourceType
from Model.Priority import Priority
from Controller.PriorityController import create_priority

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




seed_resource_types()
seed_priority()