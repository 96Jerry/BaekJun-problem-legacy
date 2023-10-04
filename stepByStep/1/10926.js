const fs = require('fs')
const filePath = process.platform === "linux" ? "/dev/stdin" : "../../input.txt"
const input = fs.readFileSync(filePath).toString().trim()

console.log(input + '??!')

// 원인은 유저 이름일 것으로 판단