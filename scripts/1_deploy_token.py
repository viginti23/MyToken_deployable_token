from brownie import MyToken
from scripts.helpful_scpripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, 'ether')


def main():
    account = get_account()
    my_token = MyToken.deploy(initial_supply, {"from": account}, publish_source=True)
    print(my_token.name())
