// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

contract Struct {

    struct MyStruct {
        string text;
        bool boolean;
    }

    // An array of structs
    MyStruct[] public structArray;

    // A mapping from address to Todo
    mapping(address => MyStruct) public addrToStruct;


    // Create a new struct
    // method 1
    function create1(string memory _text) public {
        structArray.push(MyStruct(_text, false));
    }

    // method 2
    function create2(string memory _text) public {
        structArray.push(MyStruct({text: _text, boolean: false}));
    }
  
    // method 3
    function create3(string memory _text) public {
        MyStruct memory s;
        s.text = _text;
        structArray.push(s);
    }

    // Update text
    function updateText(uint _index, string memory _text) public {
        MyStruct storage s = structArray[_index];
        s.text = _text;
    }

    // Switch Boolean
    function updateBoolean(uint _index) public {
        MyStruct storage s = structArray[_index];
        bool current = s.boolean;
        s.boolean = !current;
    }
}
