import { ethers, formatEther } from "ethers"
//import { Network, Alchemy, formatEther} from 'alchemy-sdk';

const url = 'https://mainnet.infura.io/v3/031a15bba56b472bb63f6b91918dd39f'
const provider = new ethers.JsonRpcProvider(url)

const block_number = await provider.getBlockNumber()
console.log(block_number)

const address = '0x626E05E590BbE624468C3c835922Bce0cbC71e56'
let balance = await provider.getBalance(address)

console.log(formatEther(balance))

let nonce = await provider.getTransactionCount("ethers.eth")
console.log(nonce)