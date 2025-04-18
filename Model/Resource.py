class Resource:
    def __init__(self, name: str, description: str, isAssigned: bool = False, location: str = None):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description} (Quantity: {self.quantity})"