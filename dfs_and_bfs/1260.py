# 그래프와 순회
# DFS와 BFS를 모두 구현하는 문제
import sys
from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for g in graph:
    g.sort()

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)

# # dfs, bfs
# # n : 정점의 개수, m : 간선의 개수, v : 탐색을 시작할 번호
# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     i, j = map(int, input().split())
#     graph[i].append(j)
#     graph[j].append(i)
# for i in range(1, n + 1):
#     graph[i].sort()

# dfs_visited = [v]
# bfs_visited = [v]
# q = [v]
# bfs_answer = []


# def dfs(v, visited):
#     for i in graph[v]:
#         if i not in visited:
#             visited.append(i)
#             dfs(i, visited)
#     return visited


# def bfs(visited):
#     while q:
#         next = q.pop(0)
#         for i in graph[next]:
#             if i not in visited:
#                 visited.append(i)
#                 q.append(i)
#     return visited


# print(*dfs(v, dfs_visited))
# print(*bfs(bfs_visited))
