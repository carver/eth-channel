from eth_channel.deploy import (
    launch,
)
from eth_channel.offline_pay import (
    promise_payment,
)
from eth_channel.settle_debt import (
    settle,
)
from eth_channel.web3util import (
    init_web3_dev,
)

DEFAULT_GETH_CHAIN_ID = 1337


def run_dev_demo(w3, sender, recipient, debt, chain_id):
    # sender deploys and funds the payment channel
    channel_addr = launch(w3, sender, recipient, chain_id)

    # sender signs a promise to recipient of value `debt`
    signature = promise_payment(w3, sender, recipient, debt, channel_addr, chain_id)

    # recipient claims the debt, and closes the channel
    settle(w3, recipient, channel_addr, chain_id, debt, signature)


if __name__ == '__main__':
    w3 = init_web3_dev()
    new_debt = w3.toWei('0.02', 'ether')
    chain_id = DEFAULT_GETH_CHAIN_ID

    # For the love of the FSM, don't use these keys in production:
    sender_acct = w3.eth.account.privateKeyToAccount(b'\x01' * 32)
    recipient_acct = w3.eth.account.privateKeyToAccount(b'\x02' * 32)

    run_dev_demo(w3, sender_acct, recipient_acct, new_debt, chain_id)
