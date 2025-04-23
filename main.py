from seed import seed_db
from Model.Incident import Incident
from functions import main_menu
from Controller.IncidentController import get_all_incidents

def main():
    seed_db()

    # Display the main menu and get the user's choice
    choice = main_menu()
    while choice != '5':
        if choice == '1':
            # Create an incident
            Incident.prompt_incident_data()
        elif choice == '2':
            # View incidents
            incidents = get_all_incidents()
            if incidents:
                print("Incidents:")
                for incident in incidents:
                    print(incident) # Assuming __str__ method is implemented in Incident class
            else:
                print("No incidents found.")
        elif choice == '3':
            # Update an incident
            Incident.update_incident()
        elif choice == '4':
            # Delete an incident
            Incident.delete_incident()
        else:
            print("Invalid choice. Please try again.")

        # Display the main menu again and get the user's choice
        choice = main_menu()
    print("Exiting the program. Goodbye!")

    # Create an incident 
    Incident.prompt_incident_data()


if __name__ == '__main__':
    main()

