from eth_channel.contract_info import (
    EIP191_CONTRACT_INFO,
)


def launch(w3, sender_acct, recipient_acct, chain_id):
    fund_accounts(w3, sender_acct, recipient_acct)
    contract_addr = deploy_channel(w3, sender_acct, recipient_acct, chain_id)
    deposit(w3, sender_acct, contract_addr, chain_id)
    return contract_addr


def fund_accounts(w3, sender_acct, recipient_acct):
    if w3.eth.getBalance(sender_acct.address) > 10**17:
        print("sender is already funded...")
    else:
        funder = w3.eth.accounts[0]

        print('funding sender account with 1 ETH')
        w3.eth.sendTransaction({'from': funder, 'to': sender_acct.address, 'value': 10**18})

        print('funding recipient account with 1 mETH (gas money)')
        w3.eth.sendTransaction({'from': funder, 'to': recipient_acct.address, 'value': 10**15})


def deploy_channel(w3, sender_acct, recipient_acct, chain_id):
    Channel = w3.eth.contract(**EIP191_CONTRACT_INFO)
    deploy_txn = Channel.constructor(recipient_acct.address, chain_id).buildTransaction()

    deploy_txn['nonce'] = w3.eth.getTransactionCount(sender_acct.address)
    deploy_txn['to'] = ''
    deploy_txn['chainId'] = chain_id

    signed_txn = sender_acct.signTransaction(deploy_txn)
    deployment_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    receipt = w3.eth.waitForTransactionReceipt(deployment_hash)

    contract_addr = receipt['contractAddress']
    print('deposit contract deployed at %s' % contract_addr)

    return contract_addr


def deposit(w3, sender_acct, contract_addr, chain_id):
    channel = w3.eth.contract(contract_addr, **EIP191_CONTRACT_INFO)

    deposit = 10**17
    deposit_txn = channel.functions.deposit().buildTransaction({'value': deposit})
    deposit_txn['chainId'] = chain_id
    deposit_txn['nonce'] = w3.eth.getTransactionCount(sender_acct.address)
    signed = sender_acct.signTransaction(deposit_txn)
    deposit_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

    print(f'deposited: {w3.fromWei(deposit, "ether")} eth, in transaction {deposit_hash!r}')
