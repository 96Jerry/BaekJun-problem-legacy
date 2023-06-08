# 백트래킹
# 스타트와 링크
n = int(input())

visited = [False] * n
graph = [list(map(int, input().split())) * n]
minimum = float('inf')

def dfs(depth, idx):
    global minimum
    if depth == n // 2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        minimum = min(minimum, abs(power1-power2))
        return
    
    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


dfs(0,0)
print(minimum)