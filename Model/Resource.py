class Resource:
    def __init__(self, resource_type_id: int, resource_id:int = None ):
        self.resource_id = resource_id
        self.resource_type_id = resource_type_id       

    # Getters and Setters
    def get_resource_id(self):
        return self.resource_id
    
    def get_resource_type_id(self):
        return self.resource_type_id
    
    def set_resource_id(self, resource_id:int):
        self.resource_id = resource_id

    def set_resource_type_id(self, resource_type_id:int):
        self.resource_type_id = resource_type_id
    
    # String representation of the object
    def __str__(self):
        return f"Resource(id={self.resource_id}, resource_type_id={self.resource_type_id})"
    
    # Representation of the object for debugging
    def __repr__(self):
        return f"Resource(resource_id={self.resource_id}, resource_type_id={self.resource_type_id})"