const Web3 = require('web3');

/* REPLACE: 노드 엔드포인트 문자열 */
const ENDPOINT = 'YOUR_ENDPOINT';
/* REPLACE: 배포할 EOA  */
const address = 'YOUR_EOA';
/* REPLACE: 배포할 컨트랙트의 ABI */
const abi = [{}];
/* REPLACE: 배포할 컨트랙트의 Bytecode 문자열 */
const bytecode = 'CONTRACT_BYTECODE';

// web3 인스턴스 생성
const web3 = new Web3(new Web3.providers.HttpProvider(ENDPOINT));

// Deploy contract
const deploy = async () => {
    console.log(`Attempting to deploy from account: ${address}`);
    
    //https://web3js.readthedocs.io/en/v1.3.1/glossary.html#glossary-json-interface
    const testContract = new web3.eth.Contract(abi);
 
    testContract.deploy({
        data: bytecode,
    })
    .send({
        from: address,
        gasLimit: 3000000
    })
    .on('error', error => { 
        console.log(`error: ${error}`);
     })
    .on('transactionHash', transactionHash => {
        console.log(`txHash: ${transactionHash}`) })
    .on('receipt', function(receipt){
       console.log(`CA from receipt: ${receipt.contractAddress}`) // contains the new contract address
    })
    /** it keeps watching getBlockByNumber */
    .on('confirmation', (confirmationNumber, receipt) => { 
        console.log(`confirmNo.: ${confirmationNumber}`);
        console.log(receipt);
     })
    .then(newContractInstance => {
        console.log(`CA: ${newContractInstance.options.address}`) // instance with the new contract address
    }).catch(e => console.log(e));
 };
 
 deploy();