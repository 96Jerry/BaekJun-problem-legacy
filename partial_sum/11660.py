# 부분구간합
# 2차원에서 구간합을 구하는 문제
import sys

n, m = map(int, sys.stdin.readline().split())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))
# a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
b = []
for i in range(m):
    b.append(list(map(int, sys.stdin.readline().split())))
# b = [[2,2,3,4], [3,4,3,4], [1,1,4,4]]
# print(b)

prefix = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] = (
            a[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
        )

totalList = []
for i in range(m):
    x1, y1 = b[i][0], b[i][1]
    x2, y2 = b[i][2], b[i][3]
    total = (
        prefix[x2][y2]
        - prefix[x1 - 1][y2]
        - prefix[x2][y1 - 1]
        + prefix[x1 - 1][y1 - 1]
    )
    totalList.append(total)
print(totalList)
