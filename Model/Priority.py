class Priority:
    def __init__(self, name:str, description: str, priority_id:int =None):
        self.priority_id = priority_id
        self.name = name
        self.description = description

    def get_priority_id(self):
        return self.priority_id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description