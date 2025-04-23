class IncidentEmergencyTypePriorityResource:

    def __init__(self, incident_id, emergency_type_priority_resource_id:int, incident_emergency_type_priority_resource_id:int=None):
        self.incident_emergency_type_priority_resource_id = incident_emergency_type_priority_resource_id
        self.incident_id = incident_id
        self.emergency_type_priority_resource_id = emergency_type_priority_resource_id


    # Getters and Setters
    def get_incident_emergency_type_priority_resource_id(self):
        return self.incident_emergency_type_priority_resource_id
    
    def get_incident_id(self):
        return self.incident_id
    
    def get_emergency_type_priority_resource_id(self):
        return self.emergency_type_priority_resource_id
    
    
    

