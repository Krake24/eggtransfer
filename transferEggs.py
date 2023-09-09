#!/bin/env python3
from web3 import Web3
from web3.middleware import geth_poa_middleware 
import json
from datetime import datetime
import requests
import time

#ENTER THE ABI FOR THIS CONTRACT (Instructions: https://cryptomarketpool.com/how-to-get-a-smart-contracts-abi-for-use-in-python-web3-py/)
abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"operator","type":"address"}],"name":"OperatorNotAllowed","type":"error"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"MigrateBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"MintBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_MIGRATABLE_TOKEN_ID","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MIN_MIGRATABLE_TOKEN_ID","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OPS_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"UPGRADER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"activateOperatorFilter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"deactivateOperatorFilter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getImplementation","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"migrate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"migrateBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"mintBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"numberBurned","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"numberMigrated","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"operatorFilterActive","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proxiableUUID","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"salePrice","type":"uint256"}],"name":"royaltyInfo","outputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"},{"internalType":"uint96","name":"feeNumerator","type":"uint96"}],"name":"setDefaultRoyalty","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalTokensCreated","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"stateMutability":"payable","type":"function"}]'

config = json.load(open("config.json"))

#### SEND TO ADDRESS !!!
TARGET_ADDRESS = Web3.toChecksumAddress(config['eggtarget'])

#### SEND FUNDS TO ADDRESS !!!
FUND_TARGET_ADDRESS = Web3.toChecksumAddress(config['fundtarget'])

payload={}
headers = {
  "X-API-KEY": f"{config['os_api_key']}",
}

#ENTER THE CONTRACT ADDRESS YOU WANT TO USE A METHOD ON
CONTRACT_ADDRESS = Web3.toChecksumAddress('0x58481864048671c833a0cee0d467d34534171713')

#w3 = Web3(Web3.HTTPProvider("https://polygon.llamarpc.com"))
w3 = Web3(Web3.HTTPProvider("https://polygon-bor.publicnode.com"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = w3.eth.contract(
    address=CONTRACT_ADDRESS,
    abi=abi,
)



# print(f'https://etherscan.io/address/{publicKey}')
# exit(0)

def transferToken(id, addedNonce, publicKey, privateKey):
    #ENTER THE WALLET THAT YOU WANT TO START THE TRANSACTION WITH (ONLY REQUIRED FOR WRITING METHODS)
    MY_ADDRESS = Web3.toChecksumAddress(publicKey)

    print(f'{datetime.now()} -- Transferring token {id} from {MY_ADDRESS} to {TARGET_ADDRESS}')

    ## WRITE METHOD EXAMPLE
    fun = contract.functions.safeTransferFrom(MY_ADDRESS, TARGET_ADDRESS, int(id))
    tx_data = fun.build_transaction(
        {
            'from' : MY_ADDRESS,
            'nonce' : w3.eth.get_transaction_count(MY_ADDRESS),
        }
    )

    tx_data['nonce'] = tx_data['nonce'] + addedNonce
    tx_data['maxFeePerGas'] = tx_data['maxFeePerGas'] * 2
    tx_data['maxPriorityFeePerGas'] = tx_data['maxPriorityFeePerGas'] * 2

    print(tx_data)

    print(f'{datetime.now()} -- Signing Transaction')
    tx_create = w3.eth.account.sign_transaction(tx_data, privateKey)

    print(f'{datetime.now()} -- Sending Transaction')
    tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
    print(f'{datetime.now()} -- Transaction created with hash: {tx_hash.hex()}')

    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=600)
    print(f'{datetime.now()} -- Tx successful with hash: { tx_receipt.transactionHash.hex() }')

def transferTokens(publicKey, privateKey):
    MY_ADDRESS = Web3.toChecksumAddress(publicKey)
    os_url = f"https://api.opensea.io/v2/chain/matic/account/{MY_ADDRESS}/nfts"
    try:
        response = requests.request("GET", os_url, headers=headers, data=payload, timeout=20)
    except:
        try:
            response = requests.request("GET", os_url, headers=headers, data=payload, timeout=20)
        except:
            response = requests.request("GET", os_url, headers=headers, data=payload, timeout=20)

    if 'nfts' in response.json():
        addedNonce = 0
        for asset in response.json()['nfts']:
            if Web3.toChecksumAddress(asset['contract']) == CONTRACT_ADDRESS:
                try:
                    transferToken(int(asset['identifier']), 0, publicKey, privateKey)
                except Exception as e:
                    print(e)
                    print("RETRYING IN 5 SECONDS")
                    time.sleep(5)
                    try:
                        transferToken(int(asset['identifier']), 0, publicKey, privateKey)
                    except Exception as e:
                        print(e)
                        print("RETRYING IN 5 SECONDS")
                        time.sleep(5)
                        try:
                            transferToken(int(asset['identifier']), 0, publicKey, privateKey)
                        except Exception as e:
                            print(e)
                            print("TOO MANY FAILURES. ABORTING")
                            exit(2)
                addedNonce=addedNonce+1
        if addedNonce == 0:
            print(f'{datetime.now()} -- No tokens to transfer for {publicKey}')
    else:
        print(f'{datetime.now()} -- No tokens to transfer for {publicKey}')

def transferFunds(publicKey, privateKey, fundTarget):
    print(f"{datetime.now()} -- Transferring remaining funds from {publicKey} to {fundTarget}")
    balance = w3.eth.getBalance(publicKey)
    nonce = w3.eth.getTransactionCount(publicKey)

    gas = 21000
    gasPrice = round(w3.eth.gas_price * 1.1)
    amount = balance - (gas * gasPrice)

    if amount <= gasPrice:
        print(f"insufficient funds: {amount/-(10**18)} more MATIC required")
        return

    print(f"{datetime.now()} -- Transferring {amount/10**18} MATIC from {publicKey} to {fundTarget}")

    tx_data = {
        'nonce' : nonce,
        'to' : Web3.toChecksumAddress(fundTarget),
        'value' : amount,
        'gas' : gas,
        'gasPrice' : gasPrice,
        'chainId' : 137
    }

    print(tx_data)

    print(f'{datetime.now()} -- Signing Transaction')
    tx_create = w3.eth.account.sign_transaction(tx_data, privateKey)

    print(f'{datetime.now()} -- Sending Transaction')
    tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
    print(f'{datetime.now()} -- Transaction created with hash: {tx_hash.hex()}')

    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=600)
    print(f'{datetime.now()} -- Tx successful with hash: { tx_receipt.transactionHash.hex() }')



wallets=config['wallets']
for i in range(len(wallets)):
    publicKey = Web3.toChecksumAddress(wallets[i]['publicKey'])
    privateKey = wallets[i]['privateKey']
    if (i+1 >= len(wallets)):
        fundTarget = FUND_TARGET_ADDRESS
    else:
        fundTarget = wallets[i+1]['publicKey']
    transferTokens(publicKey, privateKey)
    transferFunds(publicKey, privateKey, fundTarget)