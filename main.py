import sqlite3
from sqlite3 import Error
from datetime import datetime
from Incident import Incident
from functions import create_connection

def main():

    conn = create_connection('incident_management.db')

    Incident.prompt_incident_data(conn)


if __name__ == '__main__':
    main()

