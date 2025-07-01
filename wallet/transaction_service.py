class TransactionService:
    def __init__(self, transaction_repository):
        self.metadata = []
        self.transaction_repository = transaction_repository

    def get_wallet_transactions(self, wallet_address):
        return
