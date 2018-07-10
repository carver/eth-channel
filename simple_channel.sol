pragma solidity ^0.4.21;

// NOT FOR PRODUCTION USAGE

contract owned {
    address owner;
    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }
}

contract MicropaymentChannel191 is owned {
    event ClosingSoon(uint);
    uint256 public deposited;
    address public recipient;
    uint256 public endOfTheWorldAsWeKnowIt;
    uint256 public chainId;

    function MicropaymentChannel191(address _recipient, uint256 _chainId) public {
        recipient = _recipient;
        owner = msg.sender;
        chainId = _chainId;
    }

    function deposit() public payable {
        deposited += msg.value;
    }

    function scheduleClose() public onlyOwner {
        endOfTheWorldAsWeKnowIt = now + 3 days;
        emit ClosingSoon(endOfTheWorldAsWeKnowIt);
    }

    function close() public onlyOwner {
        require(now >= endOfTheWorldAsWeKnowIt);
        selfdestruct(owner);
    }

    function isValid(uint256 due, uint8 v, bytes32 r, bytes32 s) public view returns (bool) {
        if (msg.sender != recipient) {
            return false;
        }
        if (due > deposited) {
            return false;
        }
        bytes32 msghash = keccak256(
            bytes1(0x19), // eip 191
            bytes1(0x00), // sub-standard 0
            this,
            owner, recipient, due, chainId
        );
        return owner == ecrecover(msghash, v, r, s);
    }

    function settle(uint256 due, uint8 v, bytes32 r, bytes32 s) public {
        require(isValid(due, v, r, s));
        recipient.transfer(due);
        selfdestruct(owner);
    }
}
