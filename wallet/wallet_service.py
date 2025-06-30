class WalletService:
    def __init__(self, wallet_repository):
        self.wallet_repository = wallet_repository

    def _validate_receive(self, money):
        if money <= 0:
            return False
        else:
            return True

    def _validate_transfer(self, money):
        if money <= 0 or self.wallet.current_balance <= 0 or self.wallet.current_balance < money:
            return False
        else:
            return True

    def add_money(self, money):
        validation_response = self._validate_receive(money)
        if validation_response:
            self.wallet.current_balance += money
            return True
        else:
            return False

    def send_money(self, amount, destination_wallet):
        validation_response = self._validate_transfer(amount)
        if validation_response:
            self.wallet.current_balance -= amount
            destination_wallet.current_balance += amount
            return True
        return False

    def get_balance(self):
        return self.wallet.current_balance
