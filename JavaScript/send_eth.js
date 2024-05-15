import { ethers, formatEther, parseEther } from "ethers"
//import { Network, Alchemy, formatEther} from 'alchemy-sdk';

const url = 'HTTP://127.0.0.1:7545'
const provider = new ethers.JsonRpcProvider(url)

const address1 = '0x82151C595A0684FcBa5d8fFF334EB89BD268342e'
const address2 = '0xfba132e2968FB3eE8E1FC3fEA52C32bE1d52332B'
const signer = new ethers.Wallet('0xee7d4ac425db23e4968d2a20c03231eb8497c30d58a6edaf6bf29d4ee8fe0e85', provider);

let balance1 = await provider.getBalance(address1)
let balance2 = await provider.getBalance(address2)
console.log('bal1: ' + formatEther(balance1))
console.log('bal2: ' + formatEther(balance2))

let nonce = await provider.getTransactionCount(address1)

const tx = await signer.sendTransaction({
    to: address2,
    value: parseEther("1.0"),
    nonce: nonce
})

const receipt = await tx.wait();
//console.log(receipt)

balance1 = await provider.getBalance(address1)
balance2 = await provider.getBalance(address2)
console.log('bal1: ' + formatEther(balance1))
console.log('bal2: ' + formatEther(balance2))


