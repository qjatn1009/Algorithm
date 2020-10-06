from collections import deque
L, W = map(int, input().split())
maps = []
start = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(L):
    line = input()
    lines = []
    for j in range(W):
        if line[j] == 'L':
            start.append([i, j])
        lines.append(line[j])
    maps.append(lines)

def bfs(start_point):
    check = [[0 for _ in range(W)] for _ in range(L)]
    move = deque()
    move.append(start_point)
    check[start_point[0]][start_point[1]] = 1
    time = 0
    while move:
        ny, nx = move.popleft()

        for i in range(4):
            y = ny + dy[i]
            x = nx + dx[i]
            if 0 <= x < W and 0 <= y < L:
                if maps[y][x] == 'L' and check[y][x] == 0:
                    check[y][x] = check[ny][nx] + 1
                    move.append([y, x])
                    if time < check[y][x]:
                        time = check[y][x]
                    
    return time-1
result = 0
for i in start:
    time = bfs(i)
    if result < time:
        result = time

print(result)