class IncedentResource:
    def __init__(self, id: int, incident_id: int, resource_id: int):
        self.id = id
        self.incident_id = incident_id
        self.resource_id = resource_id

    def __repr__(self):
        return f"IncidentResource(id={self.id}, incident_id={self.incident_id}, resource_id={self.resource_id})"