from collections import deque
dy, dx = [-1, 1, 0, 0, -1, 1, -1, 1], [0, 0, -1, 1, -1, -1, 1, 1]
#북 남 서  동
n, m = map(int, input().split())
board = []
shark = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 1:
            shark.append([i, j, 0])
check = [[0 for _ in range(m)] for _ in range(n)]
def bfs(shark):
    move = deque()
    safety = 0
    for i in shark:
        move.append(i)
        check[i[0]][i[1]] = -1
    while (move):
        ny, nx, distance = move.popleft()
        for i in range(8):
            y, x = ny + dy[i], nx + dx[i]
            if 0 <= y < n and 0 <= x < m:
                if check[y][x] == 0 and board[y][x] == 0:
                    check[y][x] = distance + 1
                    move.append([y, x, distance + 1])
                    if safety < distance + 1:
                        safety = distance + 1
    return (safety)

print(bfs(shark))