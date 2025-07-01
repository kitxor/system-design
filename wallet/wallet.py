class Wallet:
    def __init__(self, id, type, user_id, status, current_balance, minimum_balance):
        self.id = id
        self.type = type
        self.status = status
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.user_id = user_id

    def get_current_balance(self):
        return self.current_balance

    def get_minimum_balance(self):
        return self.minimum_balance

    def __str__(self):
        return f"Wallet object: <id: {self.id}, user_id: {self.user_id}, balance: {self.current_balance}>"
