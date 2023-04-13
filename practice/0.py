import sys

graph = []
n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

print(graph)