class IncidentResource:
    def __init__(self, incident: int, resource: int):
        self.incident = incident
        self.resource = resource

    # Getters and Setters

    def get_incident(self):
        return self.incident
    
    def get_resource(self):
        return self.resource  

    def set_incident(self, incident: int):
        self.incident = incident
    
    def set_resource(self, resource: int):
        self.resource = resource
    
    # String representation of the object

    def __str__(self):
        return f"IncidentResource(incident_resource_id={self.incident_resource_id}, incident={self.incident}, resource={self.resource})"
    
    # Representation of the object for debugging
    def __repr__(self):
        return f"IniedentResource(incident_resource_id={self.incident_resource_id}, incident={self.incident}, resource={self.resource})"