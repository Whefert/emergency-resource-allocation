class EmergencyTypeSeverityResources:
    def __init__(self, emergency_type_id, severity_id, recommended_resource, quantity):
        self.emergency_type_id = emergency_type_id
        self.severity_id = severity_id
        self.recommended_resource = recommended_resource
        self.quantity = quantity

    def __repr__(self):
        return f"EmergencyTypeSeverityResources(emergency_type_id={self.emergency_type_id}, severity_id={self.severity_id}, recommended_resource={self.recommended_resource}, quantity={self.quantity})"