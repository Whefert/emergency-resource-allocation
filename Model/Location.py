class Location:
    def __init__(self, zone: int):
        self.zone = zone

    def get_zone(self):
        return self.zone
    
    def set_zone(self, zone: int):
        self.zone = zone

    # String representation of the object
    def __str__(self):
        return f"Location: {self.name}, Zone: {self.zone}"
    # Representation of the object for debugging
    def __repr__(self):
        return f"Location(name={self.name}, zone={self.zone})"