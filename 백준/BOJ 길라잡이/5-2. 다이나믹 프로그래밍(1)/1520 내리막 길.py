from collections import deque
m, n = map(int, input().split())
maps = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(m):
    maps.append(list(map(int, input().split())))
dp = [[-1 for _ in range(n)] for _ in range(m)]

def dfs(ny, nx):    

    if nx == n-1 and ny == m-1: 
        return 1
    if dp[ny][nx] != -1:
        return dp[ny][nx]
    dp[ny][nx] = 0
    for i in range(4):
        y = ny + dy[i]
        x = nx + dx[i]
        if 0 <= y < m and 0 <= x < n:
            if maps[y][x] < maps[ny][nx]:
                dp[ny][nx] += dfs(y, x)
    return dp[ny][nx]

print(dfs(0, 0))