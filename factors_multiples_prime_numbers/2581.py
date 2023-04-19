# 약수, 배수, 소수
# 2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 2
import math

m = int(input())
n = int(input())

arr = [1] * (n+1)
arr[0], arr[1] = 0, 0
x = math.floor(math.sqrt(n))
for i in range(2,x+1):
    if arr[i] == 1:
        k = n // i
        for j in range(2,k+1):
            arr[i * j] = 0

prime_array = []
for i in range(m, n+1):
    if arr[i] == 1:
        prime_array.append(i)

if prime_array:
    print(sum(prime_array))
    print(min(prime_array))
else:
    print(-1)