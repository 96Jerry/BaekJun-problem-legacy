# 이분탐색
# 배열 정렬 후 이분탐색으로 값 찾기
import sys

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

arr1.sort()

def binary_search (arr, x):
    start = 0
    end = n-1
    while start<=end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for el in arr2:
    print(binary_search(arr1, el))