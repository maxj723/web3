#!/usr/bin/env python3
from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/031a15bba56b472bb63f6b91918dd39f'
web3 = Web3(Web3.HTTPProvider(infura_url))

def __main__():
    
    account = '0x626E05E590BbE624468C3c835922Bce0cbC71e56'
    connected = web3.is_connected()
    


    if connected:
        balance = web3.eth.get_balance(account)
        print(balance / (10 ** 18))

if __name__ == '__main__':
    __main__()