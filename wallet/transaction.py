class Transaction:
    # id, source wallet , destination wallet, amount,
    def __init__(self, id, source_wallet_id, destination_wallet_id, amount, transfer_type, status, timestamp):
        self.id = id
        self.source_wallet_id = source_wallet_id
        self.destination_wallet_id = destination_wallet_id
        self.amount = amount
        self.transfer_type = transfer_type
        self.timestamp = timestamp
        self.status = status

    def get_source_wallet(self):
        return self.source_wallet_id
