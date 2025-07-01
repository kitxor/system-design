from user import User
from transaction_repository import TransactionRepository
from wallet_repository import WalletRepository
from wallet_service import WalletService

if __name__ == "__main__":
    wallet_repository = WalletRepository()
    transaction_repository = TransactionRepository()
    wallet_service = WalletService(wallet_repository, transaction_repository)

    tapan = User("1", "Tapan")
    aditya = User("2", "Aditya")

    print(tapan, aditya)
    # create wallet.
    tapan_wallet = wallet_service.create_wallet(tapan.id)
    aditya_wallet = wallet_service.create_wallet(aditya.id)

    print(tapan_wallet, aditya_wallet)

    # add money
    wallet_service.add_money(1000, tapan_wallet.id)
    wallet_service.add_money(1000, aditya_wallet.id)
    print(tapan_wallet, aditya_wallet)

    # move money
    wallet_service.send_money(200, tapan_wallet.id, aditya_wallet.id)
    print(tapan_wallet, aditya_wallet)

    # move money
    wallet_service.send_money(500, aditya_wallet.id, tapan_wallet.id)
    print(tapan_wallet, aditya_wallet)

    # see transactions
    tapan_history = wallet_service.get_wallet_transactions(tapan_wallet.id)
    print(tapan_history)