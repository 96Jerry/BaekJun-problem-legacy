# 다익스트라 알고리즘
# 최단경로 구하기
# 가중치가 있는 그래프
import heapq
import sys

input = sys.stdin.readline
# graph = (u,v,w) => u 에서 v 로 가는 가중치가 w인 간선이 존재
v, e = map(int, input().split())
k = int(input())
# 입력을 받아서 그 값의 첫번째 두번째 값에 대해 graph[i]  = j, graph[j] = i 그리고 세번째 값을 넣어준다. 반복.
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a = list(map(int, input().split()))
    graph[a[0]].append((a[1], a[2]))
    # graph[a[1]].append((a[0], a[2])) # 방향성이 있는 그래프이기 때문에 한번만 해준다.
INF = float("inf")
answer = [INF] * (v + 1)


def solution(graph, start, answer):
    answer[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, point = heapq.heappop(q)
        if answer[point] < dist:
            continue
        for i in graph[point]:
            cost = dist + i[1]
            if cost < answer[i[0]]:
                answer[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


solution(graph, k, answer)

for i in range(1, v + 1):
    if answer[i] == INF:
        print("INF")
    else:
        print(answer[i])
