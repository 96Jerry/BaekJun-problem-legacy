# 투 포인터
# 한 쪽에서 두 포인터를 이동시키는 문제
import sys

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
partial_sum = 0
start, end = 0, 0
min_length = float('inf')

while True:
    if partial_sum >= S:
        min_length = min(min_length, end - start)
        partial_sum -= nums[start]
        start += 1
    elif end == N:
        break
    else:
        partial_sum += nums[end]
        end += 1

if min_length != float('inf'):
    print(min_length)
else:
    print(0)