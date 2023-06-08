# 동적 계획법
# 메모이제이션, N을 1로 바꾸기, 연산 몇 번 사용하는지 계산 문제
n = int(input())

dp = [0] * (n+1)
if n > 1:
    dp[2] = 1
if n > 2:
    dp[3] = 1

for i in range(4,n+1):
    arr = []
    if i % 2 == 0:
        arr.append(dp[i//2])
    if i % 3 == 0:
        arr.append(dp[i//3])
    arr.append(dp[i-1])
    
    dp[i] = min(arr) + 1

print(dp[-1])