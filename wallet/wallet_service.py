import random

from wallet.transaction import Transaction


class WalletService:
    def __init__(self, wallet_repository, transaction_repository):
        self.wallet_repository = wallet_repository
        self.transaction_repository = transaction_repository

    def _validate_transfer(self, money, source_wallet, destination_wallet):
        if source_wallet is None:
            return {"status": False, "message": "Source wallet not found"}

        if destination_wallet is None:
            return {"status": False, "message": "Destination wallet not found"}

        if source_wallet.current_balance < money:
            return {"status": False, "message": "Not enough funds"}

        if money == 0:
            return {"status": False, "message": "Minimum transfer funds is X"}

        return {"status": True, "message": "safe to make transfer"}

    # to your own wallet
    def add_money(self, money, wallet_id):
        wallet = self.wallet_repository.get_wallet(wallet_id)
        if wallet is None:
            return False
        if money > 0:
            wallet.current_balance += money
            transaction = Transaction(random.randint(1, 10000), "SELF_SOURCE", wallet_id, money, "CREDIT", "SUCCESS",
                                      "timestamp")
            self.transaction_repository.create_transaction(transaction)
            return True

        return False

    def send_money(self, amount, source_wallet_id, destination_wallet_id):
        source_wallet = self.wallet_repository.get_wallet_by_id(source_wallet_id)
        destination_wallet = self.wallet_repository.get_wallet_by_id(destination_wallet_id)
        validation_response = self._validate_transfer(amount, source_wallet, destination_wallet)
        if validation_response.get("status"):
            source_wallet.current_balance -= amount
            destination_wallet.current_balance += amount
            transaction = Transaction(random.randint(1, 10000), source_wallet_id, destination_wallet_id, amount,
                                      "DEBIT",
                                      "SUCCESS",
                                      "timestamp")
            self.transaction_repository.create_transaction(transaction)
            return True

        return False

    def get_wallet_transactions(self, wallet_id):
        return self.transaction_repository.get_wallet_transactions(wallet_id)
