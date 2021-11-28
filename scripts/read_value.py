from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1]
    val = simple_storage.retrieve()
    print(val)

def main():
    read_contract()