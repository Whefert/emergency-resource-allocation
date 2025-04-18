import sqlite3
from sqlite3 import Error
from datetime import datetime
from Incident import Incident

def main():
    Incident.prompt_incident_data()


if __name__ == '__main__':
    main()

