# 심화
import sys

input = sys.stdin.readline
c = int(input())
answer = []
arr2 = []
for _ in range(c):
    arr = list(map(int, input().split()))
    arr2.append(arr)


for arr in arr2:
    n = arr[0]
    average = sum(arr[1:n+1]) / n
    count = 0
    for j in range(1, n+1):
        if arr[j] > average:
            count += 1
    percent = (count * 100 / n)
    result = round(percent, 3)
    print(f"{result:.3f}%")