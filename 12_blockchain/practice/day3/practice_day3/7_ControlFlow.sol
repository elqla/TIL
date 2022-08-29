// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

contract IfElse {
    function foo(uint x) public pure returns (uint) {
        if (x < 10) {
            return 0;
        } else if (x < 20) {
            return 1;
        } else {
            return 2;
        }
    }

    function ternary(uint _x) public pure returns (uint) {
        return _x < 10 ? 1 : 2;
    }
}

contract Loop {
    function loop1() public pure {
        for (uint i = 0; i < 10; i++) {
            if (i == 3) {
                continue;
            }
            if (i == 5) {
                break;
            }
        }
    }

    function loop2() public pure {
        uint i;
        while (i < 10) {
            i++;
        }
    }
}
