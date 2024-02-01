#!/usr/bin/env python3
import json
from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/031a15bba56b472bb63f6b91918dd39f'
web3 = Web3(Web3.HTTPProvider(infura_url))

json_file = 'test_abi.json'
address = '0x1c946039B8fb3BB8527981eccA8aA9d103ce389D'

def __main__():

    with open(json_file) as abi:
        data = json.load(abi)
        abi_arr = data['abi']
    
    contract = web3.eth.contract(address=address, abi=abi_arr)

    totalSupply = contract.functions.maxSupply().call()
    print(totalSupply)

if __name__ == '__main__':
    __main__()