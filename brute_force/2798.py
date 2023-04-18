# 브루트 포스
# 세 장의 카드를 고르는 모든 경우를 고려하는 문제
from itertools import combinations as cb

n, m = map(int, input().split())
nums = list(map(int, input().split()))

arr = []
for el in cb(nums, 3):
    if sum(el) <= m:
        arr.append(sum(el))

result = max(arr)
print(result)