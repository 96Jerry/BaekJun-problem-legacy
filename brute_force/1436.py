# 브루트 포스
# N번째 종말의 수가 나올 때까지 차례대로 시도하는 문제
n = int(input())

arr = []
a = 666
while len(arr) <= n:
    if '666' in str(a):
        arr.append(a)
    a += 1

print(arr[-2])