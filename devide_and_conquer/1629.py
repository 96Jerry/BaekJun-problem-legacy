# 분할정복
# 거듭제곱을 빠르게 계산하는 문제
import sys

array = list(map(int, sys.stdin.readline().split()))
a = array[0]
b = array[1]
c = array[2]

def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = power(x,n//2)
        return (temp*temp)%c
    else:
        return (x * power(x, n-1))%c
result = power(a,b) % c
    


print(result)