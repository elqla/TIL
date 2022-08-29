// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

contract FundRaising {
    uint256 public constant MINIMUM_AMOUNT = 1e16; //최소 모금액 0.01eth
    uint256 public fundRaisingCloses; //모금종료시간 (uint duration 몇초동안 모금이 유효한지 의미 3600 = 1시간, 3600*24 = 하루)
    address public beneficiary; //모금 수령자

    mapping(address => uint256) funderToAmount;
    address[] funders; //모금자

    // 컨트랙트 배포시 호출되는 함수
    constructor(uint256 _duration, address _beneficiary) {
        //block.timestamp - 현재블록의 시간?
        fundRaisingCloses = block.timestamp + _duration;
        beneficiary = _beneficiary;
    }

    //모금
    function fund() public payable {
        //if문이 아닌, require문을 사용
        require(msg.value >= MINIMUM_AMOUNT, "MINIMUM_AMOUNT: 0.01 ether");
        require(block.timestamp < fundRaisingCloses, "FUND RAISING CLOSED");

        addFunder(msg.sender);
        //msg.sender의 주소를 funder라는 변수에 선언
        //address funder = msg.sender;
        funderToAmount[msg.sender] += msg.value;
    }

    function addFunder(address _funder) internal {
        if (funderToAmount[_funder] == 0) {
            funders.push(_funder);
        }
    }

    //현재까지 모금된 금액 누구나 확인 가능
    function currentCollection() public view returns (uint256) {
        //view == 읽기만 하는 함수
        if (address(this) == address(0)) return 0;
        return address(this).balance; //현재 address(this이 사람 이 주소가 가지고 있는 이더가 얼마만큼인지)).balance
    }

    modifier onlyBeneficiary() {
        require(msg.sender == beneficiary, "NOT BENEFICIARY ADDRESS");
        _; // 언더바 === 다시 함수로 돌아간다는 의미 !
    }

    modifier onlyAfterFundCloses() {
        require(block.timestamp > fundRaisingCloses, "FUND NOT CLOSES YET");
        _;
    }

    //구매 완료시 실행(수혜자만 실행할 수 있어야 함)
    //payable 지불가능한
    function withdraw() public payable onlyBeneficiary onlyAfterFundCloses {
        //send와 transfer는 address payable타입에서 사용 가능
        //transfer의 사용 주체는 msg.sender라서 감싸줌 !
        payable(msg.sender).transfer(address(this).balance);
    }

    function selectRandomFunder() public view returns (address, uint256) {
        if (funders.length == 0) return (address(0), 0);

        bytes32 rand = keccak256(abi.encodePacked(blockhash(block.number)));
        address selected = (funders.length == 1)
            ? funders[0]
            : funders[uint256(rand) % funders.length];
        return (selected, funderToAmount[selected]);
    }
}
