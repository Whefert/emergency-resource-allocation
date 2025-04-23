class EmergencyTypePriorityResource:
    def __init__(self, emergency_type_id:int, priority_id:int, recommended_resource_type_id:int, recommended_quantity: int, emergency_type_priority_resource_id:int=None):
        self.emergency_type_priority_resource_id = emergency_type_priority_resource_id
        self.emergency_type_id = emergency_type_id
        self.priority_id = priority_id
        self.recommended_resource_type_id = recommended_resource_type_id
        self.recommended_quantity = recommended_quantity

    # Getters and Setters
    def get_emergency_type_severity_resources_id(self):
        return self.emergency_type_priority_resource_id
    
    def get_emergency_type_id(self):
        return self.emergency_type_id
    
    def get_priority_id(self):
        return self.priority_id
    
    def get_recommended_resource_type_id(self):
        return self.recommended_resource_type_id
    
    def get_recommended_quantity(self):
        return self.recommended_quantity
    
    def set_emergency_type_priority_resources_id(self, emergency_type_priority_resources_id:int):
        self.emergency_type_priority_resource_id = emergency_type_priority_resources_id    

    def set_emergency_type_id(self, emergency_type_id:int):
        self.emergency_type_id = emergency_type_id
    
    def set_priority_id(self, priority_id:int):
        self.priority_id = priority_id
    
    def set_recommended_resource_type_id(self, recommended_resource_type_id:int):
        self.recommended_resource_type_id = recommended_resource_type_id
    
    def __repr__(self):
        return f"EmergencyTypeSeverityResource(emergency_type_severity_resources_id={self.emergency_type_priority_resource_id}, emergency_type_id={self.emergency_type_id}, priority_id={self.priority_id}, recommended_resource_type_id={self.recommended_resource_type_id}, recommended_quantity={self.recommended_quantity})"
    
    def __str__(self):
        return f"EmergencyTypeSeverityResource(emergency_type_severity_resources_id={self.emergency_type_priority_resource_id}, emergency_type_id={self.emergency_type_id}, priority_id={self.priority_id}, recommended_resource_type_id={self.recommended_resource_type_id}, recommended_quantity={self.recommended_quantity})"