class Status:
    def __init__(self, name:str, description:str, status_id:int=None):  

        self.status_id = status_id
        self.name = name
        self.description = description

    # Getters and Setters
    def get_status_id(self):
        return self.status_id
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def set_status_id(self, status_id):
        self.status_id = status_id
    
    def set_name(self, name):
        self.name = name
    
    def set_description(self, description):
        self.description = description
    
    # String representation of the object
    def __str__(self):
        return f"Status ID: {self.status_id}, Status Name: {self.name}, Description: {self.description}"

    # Representation of the object for debugging
    def __repr__(self):
        return f"Status(status_id={self.status_id}, name='{self.name}')"
