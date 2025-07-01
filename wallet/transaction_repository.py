class TransactionRepository:
    def __init__(self):
        self.transactions = []

    def create_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_wallet_transaction(self, wallet_id):
        result = []
        for txn in self.transactions:
            if txn.source_wallet_id == wallet_id or txn.destination_wallet_id == wallet_id:
                result.append(txn)

        return result
