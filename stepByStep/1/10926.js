const fs = require('fs')
const filePath = process.platform === "linux" ? "/dev/stdin" : "../../input.txt"
const input = fs.readFileSync(filePath).toString().trim()

console.log(input + '??!')

// github 설정 오류로 잔디가 심어지지 않는 문제 발생