from seed import seed_db
from functions import main_menu

from Model.Incident import Incident

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
            Incident.show_all_incidents()
          # 
        elif choice == '3':
            # Update an incident
            return
            # Incident.update_incident()
        elif choice == '4':
            return
            # Delete an incident
            # Incident.delete_incident()
        else:
            print("Invalid choice. Please try again.")

        # Display the main menu again and get the user's choice
        choice = main_menu()
    print("Exiting the program. Goodbye!")

    # Create an incident 
    Incident.prompt_incident_data()


if __name__ == '__main__':
    main()

