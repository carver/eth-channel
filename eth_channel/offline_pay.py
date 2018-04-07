import time

from cytoolz import (
    assoc,
)
from eth_utils import (
    hexstr_if_str,
    keccak,
    remove_0x_prefix,
    to_bytes,
    to_hex,
)

from eth_channel.contract_info import (
    EIP191_CONTRACT_INFO,
)


def promise_payment(w3, sender, recipient, new_debt, channel_addr, chain_id):
    channel = w3.eth.contract(channel_addr, **EIP191_CONTRACT_INFO)

    message_hash = offline_payment_hash(channel, sender, recipient, new_debt, chain_id)

    signed = sender.signHash(message_hash)
    v, r, s = signed.v, signed.signature[:32], signed.signature[32:64]

    valid = channel.functions.isValid(new_debt, v, r, s).call({'from': recipient.address})

    print(f'message is valid? {valid} for {new_debt} wei, signed {to_hex(signed.signature)}')

    return signed.signature


def offline_payment_hash(channel, sender, recipient, new_debt, chain_id):
    message = (
        # EIP 191
        b'\x19',
        b'\x00',
        channel.address,
        # a message format I made up for the contract:
        sender.address,
        recipient.address,
        to_bytes(new_debt).rjust(32, b'\0'),
        to_bytes(chain_id).rjust(32, b'\0'),
    )

    message_bytes = b''.join(hexstr_if_str(to_bytes, part) for part in message)
    return keccak(message_bytes)
