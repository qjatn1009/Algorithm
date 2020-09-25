from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m, f = map(int, input().split())
road, passenger = [[1]*(n+1)], []
p, possible = [0] * m, True
for i in range(n):
    road.append([1]+ list(map(int, input().split())))
start = list(map(int, input().split()))

for i in range(m):
    psy, psx, pey, pex = map(int, input().split())
    passenger.append([psy, psx, pey, pex])
passenger.sort()

def select_passenger(sy, sx, p_start): # 승객 찾기
    visit = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    move = deque()
    visit[sy][sx] = 1
    move.append([sy, sx])
    fu, num = 100, -1
    while move:
        sy, sx = move.popleft()
        
        for i in range(4):
            y = sy + dy[i]
            x = sx + dx[i]
            if 1 <= x <= n and 1 <= y <= n:
                if road[y][x] == 0 and visit[y][x] == -1:
                    visit[y][x] = visit[sy][sx] + 1
                    move.append([y, x])
    for i in range(m):
        py, px = p_start[i][:2]
        if fu > visit[py][px]-1 and p[i] == 0:
            fu = visit[py][px] -1
            start[0], start[1] = py, px
            num = i
    if fu >= 0:
        p[num] = 1
        return fu, num
    else:
        return -1, -1

def passenger_move(sy, sx, end):
    visit = [[0 for _ in range(n+1)] for _ in range(n+1)]
    move = deque()
    move.append([sy, sx])
    visit[sy][sx] = 1
    while move:
        sy, sx = move.popleft()
        if sy == end[0] and sx == end[1]:
            start[0], start[1] = end[0], end[1]
            return visit[sy][sx] -1
        for i in range(4):
            y = sy + dy[i]
            x = sx + dx[i]
            if 1 <= x <= n and 1 <= y <= n:
                if road[y][x] == 0 and visit[y][x] == 0:
                    visit[y][x] = visit[sy][sx] + 1
                    move.append([y, x])
    
    return -1

for i in range(m):
    f1, num = select_passenger(start[0], start[1], passenger)
    f -= f1
    if f < 0 or f1 < 0:
        possible = False
        break
    f1 = passenger_move(start[0], start[1], passenger[num][2:])
    f -= f1
    if f < 0 or f1 < 0:
        possible = False
        break
    else:
        f += f1*2
if possible:
    print(f)
else:
    print(-1)