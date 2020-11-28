import time
n, m = map(int, input().split())
move = [list(map(int, input().split()))]
direction = [(0, 3), (1, 0), (2, 1), (3, 2)]
direction = [3, 0, 1, 2]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# 북 동 남 서
# 0  1  2  3
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
check = [[0 for i in range(m)] for i in range(n)]
check[move[0][0]][move[0][1]] = 1
result, count = 1, 0
while(True):
    ny, nx, dire = move.pop()
    dire = direction[dire]
    x = nx + dx[dire]
    y = ny + dy[dire]
    if 0 <= x < m and 0 <= y < n:
        if board[y][x] == 0 and check[y][x] == 0:
            check[y][x] = 1
            result += 1
            count = 0
            move.append([y, x, dire])
        else:
            move.append([ny, nx, dire])
            count += 1
    else:
        move.append([ny, nx, dire])
        count += 1
    if count == 4:
        x = nx - dx[dire]
        y = ny - dy[dire]
        if board[y][x] == 1:
            break
        else:
            count = 0
            move.append([y, x, dire])
print(result)