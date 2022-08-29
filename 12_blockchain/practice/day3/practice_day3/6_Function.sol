// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

contract Function {

    uint public num = 1;

    uint public a = 1;
    string public s = "hello solidity";
    bool public b = true;

    // No parameter and return value
    function addOne() public {
        num++;
    }

    // One parameter and a return value
    function addNumber(uint x) public returns (uint) {
        num += x;

        return num;
    }
 
    // view - not to modify the state variable, but read.
    function addAndReturn(uint x) public view returns (uint) {
       return num + x;
    }

    // pure - not to modify or read the state variable.
    function add(uint x, uint y) public pure returns (uint) {
       return x + y;
    }

    // Return many values
    function returnMany() public view returns (uint, string memory, bool) {
        return (a, s, b);
    }

}
