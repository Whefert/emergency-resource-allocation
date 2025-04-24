def main_menu():
    """
    Display the main menu and return the user's choice.
    """
    print("Main Menu")
    print("1. Create Incident")
    print("2. View Incidents")
    print("3. Update Incident")
    print("4. Delete Incident")
    print("5. Exit")

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