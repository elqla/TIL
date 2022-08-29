// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

contract Mapping {
    // Mapping from address to uint
    mapping(address => uint) public addrToUint;

    // Access value with key in Mapping.
    // If there is no key, it will return the default value, 0.
    function get(address _addr) public view returns (uint) {
        return addrToUint[_addr];
    }

    // Update the value at the address
    function set(address _addr, uint _i) public {
        addrToUint[_addr] = _i;
    }

    // Reset the value to the default value.
    function reset(address _addr) public {
        delete addrToUint[_addr];
    }
}