from collections import deque
n = int(input())
m, max_h = [], 0
for i in range(n):
    height = list(map(int, input().split()))
    if max(height) > max_h:
        max_h = max(height)
    m.append(height)
result = [0] * max_h
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(row, col, h):
    p = deque()
    p.append([row, col])
    visit[col][row] = 1
    while p :
        nx, ny = p.popleft()
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if m[y][x] > h and visit[y][x] == 0:
                    visit[y][x] = 1
                    p.append([x, y])
    result[h] += 1
for i in range(max_h):
    visit = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if m[j][k] > i and visit[j][k] == 0:
                bfs(k, j, i)
print(max(result))