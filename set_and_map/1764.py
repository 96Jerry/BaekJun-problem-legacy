# 집합과 맵
# 겹치는 값 찾기
from collections import Counter
n, m = map(int, input().split())

arr1, arr2 = [], []
for i in range(n):
    arr1.append(input())
for i in range(m):
    arr2.append(input())

a = set(arr1) & set(arr2)

result = list(a)
result.sort()
print(len(result))
for i in result:
    print(i)