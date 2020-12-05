from itertools import combinations
from copy import deepcopy
from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
n, m = map(int, input().split())
board = []
possible_wall = []
virus = []
answer = 0
# 0 : 빈 칸 1 : 벽 2 : 바이러스
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 0:
            possible_wall.append([i, j])
        elif board[i][j] == 2:
            virus.append([i, j])

safety = len(possible_wall) - 3
result = 0

def bfs(arr, virus, safety):
    move = deque(virus)
    while (move): 
        ny, nx = move.popleft()
        for i in range(4):
            y = ny + dy[i]
            x = nx + dx[i]
            if 0 <= y < n and 0 <= x < m:
                if arr[y][x] == 0:
                    arr[y][x] = 2
                    safety -= 1
                    move.append([y, x])
    return (safety)

for select in list(combinations(possible_wall, 3)):
    arr = deepcopy(board)
    for j in select:
        arr[j[0]][j[1]] = 1
    result = max(result, bfs(arr, virus, safety))
print(result)