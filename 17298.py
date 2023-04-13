# 스택 2
# 스택을 사용하여 답의 후보를 오름/내림차순으로 관리하는 문제
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
arr = [-1]*N

stack = []
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        idx = stack.pop()
        arr[idx] = A[i]
    stack.append(i)
    
print(arr)