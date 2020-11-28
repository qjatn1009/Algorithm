from collections import deque
n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, input())))
check = [[0 for i in range(m)] for i in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = 0
# dfs
def dfs(ny, nx):
    check[ny][nx] = 1
    for i in range(4):
        y = ny + dy[i]
        x = nx + dx[i]
        if 0 <= y < n and 0 <= x < m:
            if ice[y][x] == 0 and check[y][x] == 0:
                dfs(y, x)
    return (1)
for i in range(n):
    for j in range(m):
        if ice[i][j] == 0 and check[i][j] == 0:
            result += dfs(i,j)
print(result)
# bfs
def bfs(ny, nx, result):
    move = deque()
    move.append([ny, nx])
    while (move):
        ny, nx = move.popleft()
        check[ny][nx] = 1
        for i in range(4):
            y = ny + dy[i]
            x = nx + dx[i]
            if 0 <= y < n and 0 <= x < m:
                if ice[y][x] == 0 and check[y][x] == 0:
                    move.append([y, x])
                    check[y][x] = 1
    result += 1
    return (result)

for i in range(n):
    for j in range(m):
        if ice[i][j] == 0 and check[i][j] == 0:
            result = bfs(i, j, result)
print(result)
