class EmergencyType:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"EmergencyType(id={self.id}, name='{self.name}')"

    def __repr__(self):
        return self.__str__()