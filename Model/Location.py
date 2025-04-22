class Location:
    def __init__(self, zone: int, x_coordinate: float, y_coordinate: float, location_id: int = None):
        self.zone = zone
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.location_id = location_id

    # Getters and Setters
    def get_zone(self):
        return self.zone
    
    def set_zone(self, zone: int):
        self.zone = zone

    def get_x_coordinate(self):
        return self.x_coordinate
    
    def set_x_coordinate(self, x_coordinate: float):
        self.x_coordinate = x_coordinate

    def get_y_coordinate(self):
        return self.y_coordinate

    def set_y_coordinate(self, y_coordinate: float):
        self.y_coordinate = y_coordinate
    
    def get_location_id(self):
        return self.location_id
    
    def set_location_id(self, location_id: int):
        self.location_id = location_id

    # String representation of the object
    def __str__(self):
        return f"Location(id={self.location_id}, zone={self.zone}, x_coordinate={self.x_coordinate}, y_coordinate={self.y_coordinate})"
    # Representation of the object for debugging
    def __repr__(self):
        return f"Location(zone={self.zone}, x_coordinate={self.x_coordinate}, y_coordinate={self.y_coordinate})"