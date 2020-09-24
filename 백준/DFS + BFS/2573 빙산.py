from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, input().split())))
# 빙산이 분리되는 최초의 시간 다 녹을때까지 분리 안되면 0
def melt(nx, ny): # 빙하가 녹은 후
    for i in range(4):
        x = nx + dx[i]
        y = ny + dy[i]
        if 0 <= x < m and 0 <= y < n :
            if ice[y][x] == 0 and visit[y][x] == 0:
                visit[ny][nx] = 1
                if ice[ny][nx] == 0:
                    ice[ny][nx] = 0
                else:
                    ice[ny][nx] -= 1
    

def check_bfs(row, col): # 분리 됐는지 안됐는지 검사
    check = deque()
    check.append([row, col])
    ice_check[col][row] = 1
    while check:
        nx, ny = check.popleft()
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if 0 <= x < m and 0 <= y < n :
                if ice[y][x] > 0 and ice_check[y][x] == 0:
                    ice_check[y][x] = 1
                    check.append([x, y])

result = 0
while True:
    cnt = 0
    visit = [[0 for _ in range(m)] for _ in range(n)]
    ice_check = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(n):
        for k in range(m):
            if ice[j][k] != 0 and ice_check[j][k] == 0:
                check_bfs(k, j)
                cnt += 1
    for j in range(n):
        for k in range(m):
            if ice[j][k] != 0:
                melt(k, j)
    if cnt == 0:
        print(0)
        break
    elif cnt >= 2:
        print(result)
        break
    result+= 1