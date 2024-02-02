#!/usr/bin/env python3
from web3 import Web3

node_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(node_url))

account_1 = '0xF6d4bA9487542c2FF012b8890F2AF3fA46065c5c'
account_2 = '0xF366120a86544215848F06e7AE2Dc5FC4CfC8710'
private_key_1 = '0x4132db49246a043df5992d7b8164e2e760c2dc107ac6119eed6b1091f14e95ec'
private_key_2 = '0xfd19f45b1c90f4bd0f8fbea9573b90d910b6a1064f68cc9adc9af0dbe85c315e'

def __main__():

    nonce = web3.eth.get_transaction_count(account_1)

    tx = {
        'nonce': nonce,
        'to': account_2,
        'value': web3.to_wei(1, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei'),
    }

    signed_tx = web3.eth.account.sign_transaction(tx, private_key_1)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(web3.to_hex(tx_hash))

    
if __name__ == '__main__':
    __main__()