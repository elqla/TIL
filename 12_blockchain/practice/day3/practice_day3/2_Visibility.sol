// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Parent {
    // State variables
    string private privateVar = "private variable";
    string internal internalVar = "internal variable";
    string public publicVar = "public variable";
    
    // Private function 
    function privateFunc() private pure returns (string memory) {
        return "private function called";
    }

    function testPrivateFunc() public pure returns (string memory) {
        return privateFunc();
    }

    // Internal function 
    function internalFunc() internal pure returns (string memory) {
        return "internal function called in Parent Contract";
    }

    function testInternalFunc() public pure virtual returns (string memory) {
        return internalFunc();
    }

    // Public functions
    function publicFunc() public pure returns (string memory) {
        return "public function called";
    }

    // External functions 
    function externalFunc() external pure returns (string memory) {
        return "external function called";
    }
}

contract Child is Parent {
    // Internal function call be called inside child contracts.
    function testInternalFunc() public pure override returns (string memory) {
        return internalFunc();
    }
}
