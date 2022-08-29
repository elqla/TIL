// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

contract Struct {

    struct Todo {
        string text;
        bool completed;
    }

    Todo[] public todos;

    function create(string memory _text) public {
        todos.push(Todo(_text, false));
    }

    // if todos array is declared as public, solidity will generate this function automatically.
    function get(uint _index) public view returns (string memory text, bool completed) {
        Todo storage todo = todos[_index];
        return (todo.text, todo.completed);
    }

    function update(uint _index, string memory _text) public {
        Todo storage todo = todos[_index];
        todo.text = _text;
    }

    function toggle(uint _index) public {
        Todo storage todo = todos[_index];
        todo.completed = !todo.completed;
    }
}
