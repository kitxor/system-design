class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def __str__(self):
        return f"User object: <{self.id}: {self.name}>"