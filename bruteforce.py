import bitcoinlib
import requests
import os

address_to_hack = input("Which address do you want to hack ? ")

i = 0

while True:

    wallet = bitcoinlib.wallets.Wallet('WalletName')
    i += 1
    print("[{}] {}".format(i, wallet.get_key().address))
    if wallet.get_key().address == address_to_hack:

        print("   => Hacked ! Private key : {}".format(wallet.get_wif_uncompressed()))
        break

    i += 1
    print("[{}] {}".format(i, wallet.get_key().address))
    if wallet.get_address_compressed() == address_to_hack:
        print("   => Hacked ! Private key : {}".format(wallet.get_wif_compressed()))
        break

os.system("pause")
