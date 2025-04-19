import sqlite3
from sqlite3 import Error
from datetime import datetime
from Model.Incident import Incident
from database import create_connection

def main():
    # Create an incident 
    Incident.prompt_incident_data()



if __name__ == '__main__':
    main()

