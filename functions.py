def main_menu():
    """
    Display the main menu and return the user's choice.
    """
    print("Main Menu")
    print("1. Manage Incident")
    print("2. Manage Resource")
    print("3. Manage Emergency Type")
    print("4. Manage Priority")
    print("5. Manage Status")
    print("6. Manage Location")
    print("7. Exit")

    choice = input("Enter your choice: ")
    return choice


def incident_menu():
    """
    Display the incident menu and return the user's choice.
    """
    print("Incident Menu")
    print("1. Create Incident")
    print("2. View Incidents")
    print("3. Update Incident")
    print("4. Delete Incident")
    print("5. Exit")

    choice = input("Enter your choice: ")
    return choice


def update_incident_menu():
    """
    Display the update incident menu and return the user's choice.
    """
    print("Update Incident Menu")
    print("1. Update Location")
    print("2. Update Description")
    print("3. Update Status")
    print("4. Update Resources")
    print("5. Update Priority")
    print("7. Update Emergency Type")
    print("8. Exit")
    choice = input("Enter your choice: ")
    return choice


def resource_menu():
    """
    Display the resource menu and return the user's choice.
    """
    print("Resource Menu")
    print("1. Add Resource")
    print("2. View Resources")
    print("3. Update Resource")
    print("4. Delete Resource")
    print("5. Exit")

    choice = input("Enter your choice: ")
    return choice