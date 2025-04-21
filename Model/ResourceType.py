class ResourceType:
    """
    Represents a resource type in the system.
    """
    def __init__(self, name: str, description: str, resource_type_id:int = None):
        self.resource_type_id = resource_type_id
        self.name = name
        self.description = description

    # Getters and Setters
    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name

    def get_description(self):
        return self.description
    
    def set_description(self, description: str):
        self.description = description


    def get_resource_type_id(self):
        return self.resource_type_id

    def __repr__(self):
        return f"ResourceType(name={self.name}, description={self.description})"