// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Array {
    // Dynamic sized array
    uint[] public arr; // Not initialized
    uint[] public arr2 = [1, 2, 3]; // Initialized
    // Fixed sized array, all elements initialize to 0
    uint[10] public fixedSizeArr;

    // Compare with accessing state variable
    function get(uint i) public view returns (uint) {
        return arr2[i];
    }

    // Append new element to array
    // Check array size after calling this function.
    function push(uint i) public {
        arr.push(i);
    }

    // Remove last element from array
    // Check array size after calling this function.
    function pop() public {
        arr.pop();
    }

    // Reset the value at index
    // Check array size after calling this function.
    function remove(uint index) public {
        delete arr[index];
    }

    // returns the length of array.
    function getLength() public view returns (uint) {
        return arr.length;
    }

    // returns the entire array.
    function getArr() public view returns (uint[] memory) {
        return arr;
    }

    function createArray() external pure returns (uint[] memory){
        // create array in memory, only fixed size can be created
        uint[] memory a = new uint[](5);
        return a;
    }
}
