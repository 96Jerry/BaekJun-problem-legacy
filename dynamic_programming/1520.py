# 동적 계획법 2
# 내리막길로만 이동하는 경우의 수를 구하는 문제
import sys

m, n = map(int,sys.stdin.readline().split())
matrix = []
for i in range(m):
    matrix.append(list(map(int,sys.stdin.readline().split())))
dp = [[-1]*n for _ in range(m)]

def dfs(x,y,m,n,matrix,dp):
    if x == n-1 and y == m-1: # 목적지에 도달한 경우
        return 1
    if dp[y][x] == -1: # 중복 계산 방지
        dp[y][x] = 0
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and matrix[ny][nx] < matrix[y][x]:
                dp[y][x] += dfs(nx,ny,m,n,matrix,dp)
    return dp[y][x]

result = dfs(0,0,m,n,matrix,dp)
print(result)