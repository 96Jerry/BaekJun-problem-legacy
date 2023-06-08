# 동적 계획법
# 동적 계획법으로 합이 최대인 부분배열을 구하는 문제
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for i in range(1,n):
    nums[i] = max(nums[i], nums[i-1] + nums[i])

print(max(nums))