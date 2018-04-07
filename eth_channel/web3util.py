import time

from web3 import (
    IPCProvider,
    Web3,
)
from web3.middleware import (
    geth_poa_middleware,
)


def init_web3_dev():
    w3 = Web3(IPCProvider('/tmp/geth.ipc'))
    w3.middleware_stack.inject(geth_poa_middleware, layer=0)
    return w3
