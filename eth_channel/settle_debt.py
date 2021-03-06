from eth_utils import (
    to_int,
)

from eth_channel.contract_info import (
    EIP191_CONTRACT_INFO,
)


def settle(w3, recipient, channel_addr, chain_id, amount, signature):
    channel = w3.eth.contract(channel_addr, **EIP191_CONTRACT_INFO)

    v, r, s = to_int(signature[-1]), signature[:32], signature[32:64]

    txn = channel.functions.settle(amount, v, r, s).buildTransaction({
        'from': recipient.address,
        'chainId': chain_id,
    })
    txn['nonce'] = w3.eth.getTransactionCount(recipient.address)

    signed = recipient.signTransaction(txn)

    old_balance = w3.eth.getBalance(recipient.address)

    txn_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

    receipt = w3.eth.waitForTransactionReceipt(txn_hash)

    new_balance = w3.eth.getBalance(recipient.address)

    print(
        f'balance of recipient increased from '
        f'{w3.fromWei(old_balance, "ether")} to '
        f'{w3.fromWei(new_balance, "ether")} eth'
    )
    return receipt
