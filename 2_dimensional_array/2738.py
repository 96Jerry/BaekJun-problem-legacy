# 2차원 배열
# 2차원 배열끼리 더하기
import sys

n, m = map(int, sys.stdin.readline().split())
arr1 = []
arr2 = []
for _ in range(n):
    arr1.append(list(map(int, sys.stdin.readline().split())))
for _ in range(n):
    arr2.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        arr1[i][j] += arr2[i][j]
        print(arr1[i][j], end=' ')
    print()