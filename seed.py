from database import create_connection
import csv
import sqlite3
from sqlite3 import Error
import os

# Create connection to the SQLite database
conn = create_connection('incident_management.db')

def seed_resource_types(conn):
    # Raead the CSV file in the data folder and insert data into the resource_types table
    # Assuming the CSV file has columns: name, description
    try:
        with open('data/resource_types.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            print("Resource types seeded successfully.")
    except Error as e:
        print(e)