// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Primitives {

    // Unassigned variables have a default value
    bool public defaultBool; // false
    uint public defaultUint; // 0
    int public defaultInt; // 0
    address public defaultAddr; // 0x0000000000000000000000000000000000000000
    string public defaultString; // ''

    // addr value assignment
    address public addr = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;

    /*
    non negative integers
    different sizes are available
        uint8   ranges from 0 to 2 ** 8 - 1
        uint16  ranges from 0 to 2 ** 16 - 1
        ...
        uint256 ranges from 0 to 2 ** 256 - 1
    
    uint is same as uint256
    */
    uint8 public u8 = 1;
    uint public u = 123; 
    uint256 public u256 = 456;

    uint public maxUint = type(uint).max;
    uint public maxUint256 = type(uint256).max;

    /*
    integer
    different sizes are available, like uint

    int256 ranges from -2 ** 255 to 2 ** 255 - 1
    int128 ranges from -2 ** 127 to 2 ** 127 - 1
    */
    int8 public i8 = -1;
    int public i = -123; 
    int256 public i256 = 456;

    // minimum and maximum of int
    int public minInt = type(int).min;
    int public maxInt = type(int).max;

    /*
    In Solidity, the data type byte represent a sequence of bytes. 
    Two bytes types in Solidity:

     - fixed-sized byte arrays: bytes#
     - dynamically-sized byte arrays. byte[]
    */
    bytes1 a = 0xb5; //  [10110101]
    bytes1 b = 0x56; //  [01010110]  
}
