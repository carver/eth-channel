EIP191_CONTRACT_INFO = dict(
    bytecode="6060604052341561000f57600080fd5b60405160408061080e8339810160405280805190602001909190805190602001909190505081600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550806004819055505050610741806100cd6000396000f300606060405260043610610083576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063370e3a3f1461008857806343d726d6146100e95780635120c196146100fe578063887c1000146101135780639a8a05921461015c578063d0e30db014610185578063eef49ee31461018f575b600080fd5b341561009357600080fd5b6100cf600480803590602001909190803560ff1690602001909190803560001916906020019091908035600019169060200190919050506101b8565b604051808215151515815260200191505060405180910390f35b34156100f457600080fd5b6100fc6104fc565b005b341561010957600080fd5b6101116105a2565b005b341561011e57600080fd5b61015a600480803590602001909190803560ff169060200190919080356000191690602001909190803560001916906020019091905050610644565b005b341561016757600080fd5b61016f6106f7565b6040518082815260200191505060405180910390f35b61018d6106fd565b005b341561019a57600080fd5b6101a261070f565b6040518082815260200191505060405180910390f35b600080600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561021b57600091506104f3565b60197f01000000000000000000000000000000000000000000000000000000000000000260007f010000000000000000000000000000000000000000000000000000000000000002306000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff16600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168a60045460405180887effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff19167effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff19168152600101877effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff19167effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff191681526001018673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166c010000000000000000000000000281526014018573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166c010000000000000000000000000281526014018473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166c0100000000000000000000000002815260140183815260200182815260200197505050505050505060405180910390209050600181868686604051600081526020016040526040518085600019166000191681526020018460ff1660ff1681526020018360001916600019168152602001826000191660001916815260200194505050505060206040516020810390808403906000865af1151561049857600080fd5b50506020604051035173ffffffffffffffffffffffffffffffffffffffff166000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161491505b50949350505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561055757600080fd5b600354421015151561056857600080fd5b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16ff5b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156105fd57600080fd5b6203f48042016003819055507f7de16f3a95b889f396447d67699aabdb7a794c0c02c1ace2f53bff9156b9d7e26003546040518082815260200191505060405180910390a1565b610650848484846101b8565b151561065b57600080fd5b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc859081150290604051600060405180830381858888f1935050505015156106bd57600080fd5b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16ff5b60045481565b34600160008282540192505081905550565b600154815600a165627a7a723058209dab05f1bf3ef66a8ffe2370ac17e0c04473ba16fa775bac814411b193eaf01a0029",
    abi="""[
	{
		"constant": true,
		"inputs": [
			{
				"name": "due",
				"type": "uint256"
			},
			{
				"name": "v",
				"type": "uint8"
			},
			{
				"name": "r",
				"type": "bytes32"
			},
			{
				"name": "s",
				"type": "bytes32"
			}
		],
		"name": "isValid",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "close",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "scheduleClose",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "due",
				"type": "uint256"
			},
			{
				"name": "v",
				"type": "uint8"
			},
			{
				"name": "r",
				"type": "bytes32"
			},
			{
				"name": "s",
				"type": "bytes32"
			}
		],
		"name": "settle",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "chainId",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "deposit",
		"outputs": [],
		"payable": true,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "deposited",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"name": "_recipient",
				"type": "address"
			},
			{
				"name": "_chainId",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "",
				"type": "uint256"
			}
		],
		"name": "ClosingSoon",
		"type": "event"
	}
]""".replace('\t',''),
)
