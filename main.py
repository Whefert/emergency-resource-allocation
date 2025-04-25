# Jefferson Daley - #2416130
from seed import seed_db
from functions import main_menu, incident_menu, resource_menu, update_incident_menu
from Model.Incident import Incident

def main():
    seed_db()

    # Display the main menu and get the user's choice
    while True:
        choice = main_menu()    
        match choice:
            case '1':
                # Call the incident menu function
                incident_choice = incident_menu()
                while True:
                    match incident_choice:
                        case '1':
                            Incident.prompt_incident_data()
                            break
                        case '2':
                            Incident.show_all_incidents()
                            break
                        case '3':
                            Incident.show_all_incidents()
                            incident_id = input("Enter the incident ID to update: ")
                            update_choice = update_incident_menu()
                            while True:
                                match update_choice:
                                    case '1':
                                        Incident.update_incident_location(incident_id)
                                        break
                                    case '2':
                                        Incident.update_incident_description(incident_id)
                                        break
                                    case '3':
                                        Incident.update_incident_status(incident_id)
                                        break
                                    case '4':
                                        Incident.update_incident_resources(incident_id)
                                        break
                                    case '5':
                                        Incident.update_incident_priority(incident_id)
                                        break
                                    case '6':
                                        Incident.update_incident_emergency_type(incident_id)
                                        break
                                    case '7':
                                        print("Exiting the update incident menu.")
                                        update_choice = None
                                        break
                                    case _:
                                        print("Invalid choice. Please try again.")
                                        # Display the update incident menu again and get the user's choice
                            break
                        case '4':
                            Incident.delete_incident()
                            break
                        case '5':
                            print("Exiting the incident menu.")
                            choice = None
                            break
                        case _:
                            print("Invalid choice. Please try again.")
                            # Display the incident menu again and get the user's choice
                            break
                
            case "7":
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")
                # Display the main menu again and get the user's choice

if __name__ == '__main__':
    main()

