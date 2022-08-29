var web3;
const ROPSTEN_URL = 'https://ropsten.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161';
const CA = '0x1524DF7202E6cB073cdd651c12d873A51FA0AC6F';


const STORAGE_ABI = [
	{
		"inputs": [],
		"name": "retrieve",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "num",
				"type": "uint256"
			}
		],
		"name": "store",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
const privateKey = '';
var sender;
var senderAddress;
var storageContract;

window.addEventListener('load', () => {
    if( typeof web3 !== 'undefined') {
        window.web3 = new Web3(web3.currentProvider);
        alert('web3 injected');
    } else {
        window.web3 = new Web3(new Web3.providers.HttpProvider(ROPSTEN_URL));
    }
    startApp();
});

function startApp() {
    storageContract = new web3.eth.Contract(STORAGE_ABI, CA);
    sender = web3.eth.accounts.privateKeyToAccount('0x' + privateKey);
    web3.eth.accounts.wallet.add(sender);
    web3.eth.defaultAccount = sender.address;
    senderAddress = web3.eth.defaultAccount;

    document.getElementById('contractAddr').innerHTML = getAddrLink(CA);
    document.getElementById('accountAddr').innerHTML = getAddrLink(web3.eth.defaultAccount);

    retrieve();
}

function getAddrLink(addr) {
    return '<a target="_blank" href=https://ropsten.etherscan.io/address/' + addr + '>' + addr +'</a>';
}

function getTxLink(txHash) {
    return '<a target="_blank" href=https://ropsten.etherscan.io/tx/' + txHash + '>' + txHash +'</a>';
}

function getBlockLink(number) {
    return '<a target="_blank" href=https://ropsten.etherscan.io/block/' + number + '>' + number +'</a>';
}

function retrieve() {
  //.call 은 retrieve함수를 호출하겠다. (보내는이주소(필), 가스가격, 가스)
  //단순한 view함수
    storageContract.methods.retrieve().call({from: senderAddress})
    .then(result => {
        document.getElementById('storedData').innerHTML = result;
    });

    web3.eth.getBlockNumber(function(error, result){
        document.getElementById('lastBlock').innerHTML = getBlockLink(result);
    });
}


function store() {
  let newValue = document.getElementById('newValue').value;

  storageContract.methods.store(newValue).estimateGas({ gas: 3000000 }, (error, gasAmount) => {
    //send 가스 소모
    storageContract.methods.store(newValue).send({
        from: senderAddress,
        gas: 3000000,
        gasPrice: 10000000000
    }).on("transactionHash", (hash) => {
        document.getElementById('txHash').innerHTML = getTxLink(hash);
    }).on("receipt", receipt => {
        if(receipt.status){
            retrieve();
        }
    }).on("error", (error, receipt) => {
        console.error(error);
        console.log(">> receipt: ", receipt);
    });
  });
  
}