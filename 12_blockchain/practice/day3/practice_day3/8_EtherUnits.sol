// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

contract EtherUnits {
    uint public oneWei = 1 wei;
    uint public oneGwei = 1 gwei;
    uint public oneEther = 1 ether;
  
    // 1 wei is equal to 1
    bool public isOneWei = 1 wei == 1;

    // 1 ether is equal to 10^18 wei
    bool public isOneEther1 = oneEther == 1e18;

    // 1 ether is equals to 10^9 gwei.
    bool public isOneEther2 = oneEther == 10**9 * oneGwei;

    // 1 gwei is equals to 10^9 wei.
    bool public isOneGwei = oneGwei == 10**9 * oneWei;
}