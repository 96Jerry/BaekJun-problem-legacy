# 그리디 알고리즘
# 기다리는 시간의 합을 최소화하는 문제
# 값이 작은 사람이 앞에 오는 것이 유리
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

a.sort()
sum = 0
for i in range(1,n+1):
    sum += i * a[n-i]
print(sum)