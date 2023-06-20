const fs = require('fs')
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filePath).toString().trim()

const n = Number(input)

for (let i=1;i<n+1;i++){
    console.log(' '.repeat(n-i)+'*'.repeat(i))
}