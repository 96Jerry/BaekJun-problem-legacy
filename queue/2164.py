# 큐
# 큐를 사용하여 동작을 구현하는 문제
from collections import deque

def solution(n):
    queue = deque([i for i in range(1,n+1)])
    while len(queue) > 1:
        queue.popleft()
        temp = queue.popleft()
        queue.append(temp)
    answer = queue[0]
    return answer

n = int(input())
print(solution(n))