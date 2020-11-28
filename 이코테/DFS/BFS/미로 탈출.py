from collections import deque
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input())))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
# bfs
def bfs():
    move = deque()
    check = [[0 for i in range(m)] for i in range(n)]
    move.append([0, 0, 1])
    while (move):
        ny, nx, count = move.popleft()
        check[ny][nx] = 1
        if ny == n - 1 and nx == m - 1:
            return (count)
        for i in range(4):
            y = ny + dy[i]
            x = nx + dx[i]
            if 0 <= y < n and 0 <= x < m:
                if board[y][x] == 1 and check[y][x] == 0:
                    check[y][x] = 1
                    move.append([y, x, count + 1])
    return (-1)
# dfs
dfs_check = [[0 for i in range(m)] for i in range(n)]
def dfs(ny, nx, count):
    dfs_check[ny][nx] = 1
    if ny == n - 1 and nx == m - 1:
        print(count)
        return 
    for i in range(4):
        y = ny + dy[i]
        x = nx + dx[i]
        if 0 <= y < n and 0 <= x < m:
            if board[y][x] == 1 and dfs_check[y][x] == 0:
                dfs_check[y][x] = 1
                dfs(y, x, count + 1)

print(bfs())
dfs(0, 0, 1)
    