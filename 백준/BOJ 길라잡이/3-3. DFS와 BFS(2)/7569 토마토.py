from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
M, N, H = map(int, input().split())
tomato = []
move, count = deque(), 0

for i in range(H): # 층
    for j in range(N): # 세로
        t = list(map(int, input().split()))
        for k in range(M): # 가로
            if t[k] == 1:
                move.append([i,j,k])
            elif t[k] == 0:
                count += 1
        tomato.append(t)

def bfs():
    day, c = 0, 0
    while move:
        
        high, row, col = move.popleft()
        if c == count :
            return day
        
        for i in range(6):
            x = row + dx[i]
            y = col + dy[i]
            h = high + dh[i]
            if 0 <= x < N and 0 <= y < M and 0<= h < H:
                if tomato[N*h+x][y] == 0:
                    tomato[N*h+x][y] = tomato[high*N+row][col] + 1
                    c += 1
                    move.append([h,x,y])
                    if day < tomato[N*h+x][y]-1:
                        day = tomato[N*h+x][y]-1
        
    return -1

print(bfs())