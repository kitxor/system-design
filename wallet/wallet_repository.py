class WalletRepository:
    def __init__(self):
        self.wallets = {}

    def get_wallet_by_id(self, wallet_id):
        return self.wallets.get(wallet_id)

    def save_wallet(self, wallet):
        self.wallets[wallet.id] = wallet
