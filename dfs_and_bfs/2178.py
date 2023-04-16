# 그래프와 순회
# BFS의 특징은 각 정점을 최단경로로 방문한다는 것입니다. 이 점을 활용해 최단거리를 구해 봅시다.
import sys
from collections import deque

def bfs(v,w):
    distance = [[0]*m for _ in range(n)]
    queue = deque([(v,w)])
    graph[v][w] = 0
    distance[v][w] = 0
    while queue:
        (v,w) = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = v + dx, w + dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and distance[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                distance[nx][ny] = distance[v][w] + 1
    return distance[n-1][m-1] + 1

graph = []
n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

result = bfs(0, 0)
print(result)