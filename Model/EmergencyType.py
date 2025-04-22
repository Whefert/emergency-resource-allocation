class EmergencyType:
    def __init__(self, name:str, description:str=None, emergency_type_id: int=None, ):
        self.emergency_type_id = emergency_type_id
        self.name = name
        self.description = description

# Getters and Setters
    def get_emergency_type_id(self):
        return self.emergency_type_id
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description  

    def set_emergency_type_id(self, emergency_type_id):
        self.emergency_type_id = emergency_type_id
            

    def __str__(self):
        return f"EmergencyType(id={self.emergency_type_id}, name='{self.name}')"

    def __repr__(self):
        return self.__str__()