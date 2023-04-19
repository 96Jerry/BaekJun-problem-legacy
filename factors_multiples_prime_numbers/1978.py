# 약수, 배수, 소수
# 2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 1
import math
n = int(input())
a = list(map( int, input().split()))

arr = [1] * 1001
arr[0], arr[1] = 0, 0
x = math.floor(math.sqrt(1000))
for i in range(2,x+1):
    if arr[i] == 1:
        k = 1000 // i
        for j in range(2,k+1):
            arr[i * j] = 0

cnt = 0
for i in a:
    if arr[i] == 1:
        cnt+=1
print(cnt)