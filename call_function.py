#!/usr/bin/env python3
import json
from web3 import Web3

node_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(node_url))
abi = None
contract_address = None

def __main__():

    address = web3.toChecksumAddress(contract_address)
    contract = web3.eth.contract(address=address, abi=abi)

    print(contract.functions.greet().call())

    # Set a new greeting
    tx_hash = contract.functions.setGreeting('HEELLLLOOOOOO!!!').transact()
    # Wait for transaction to be mined
    web3.eth.waitForTransactionReceipt(tx_hash)
    # Display the new greeting value
    print('Updated contract greeting: {}'.format(
        contract.functions.greet().call()
    ))



if __name__ == '__main__':
    __main__()