const fs = require('fs')
const filePath = process.platform === "linux" ? "/dev/stdin" : "../../input.txt"
const input = fs.readFileSync(filePath).toString().trim()

console.log(input + '??!')

// 이메일이었던것으로 예상 변경