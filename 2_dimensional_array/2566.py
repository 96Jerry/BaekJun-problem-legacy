# 2차원 배열
# 2차원 배열 안에서 최대값 구하기
import sys

arr = []
for _ in range(9):
    arr.append(list(map(int, sys.stdin.readline().split())))

max_value = 0
for i in range(9):
    temp = max(arr[i])
    if max_value < temp:
        max_value = temp

for i in range(9):
    try:
        max_index = arr[i].index(max_value)
        print(max_value)
        print(i+1, max_index+1)
    except:
        continue