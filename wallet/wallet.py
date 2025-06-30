class Wallet:
    def __init__(self, id, type, user, status, current_balance, minimum_balance):
        self.id = id
        self.type = type
        self.status = status
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.user = user

    def get_current_balance(self):
        return self.current_balance

    def get_minimum_balance(self):
        return self.minimum_balance
