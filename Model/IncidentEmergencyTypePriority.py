class IncidentEmergencyTypePriority:
    def __init__(self, incident_id:int, emergency_type:int, priority:int=None):
        self.incident_id = incident_id
        self.emergency_type = emergency_type
        self.priority = priority

    # Getters and Setters
    def set_incident_id(self, incident_id:int):
        self.incident_id = incident_id

    def set_emergency_type(self, emergency_type:int):
        self.emergency_type = emergency_type
    
    def set_priority(self, priority:int):
        self.priority = priority
    
    def get_incident_id(self):
        return self.incident_id
    
