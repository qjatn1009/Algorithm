from collections import deque
N, M = map(int, input().split())
r, c, d = map(int, input().split()) # 시작 [r, c]
dx = [-1, 0, 1, 0]  # 서 남 동 북 순이네
dy = [0, 1, 0, -1]  # 3  2  1  0
dd = [[0,1,2,3],[3,0,1,2],[2,3,0,1],[1,2,3,0]]
area = []
visit = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    dp = list(map(int, input().split()))
    area.append(dp)

def bfs():
    move = deque()
    move.append([r, c, d, 1]) 
    visit[r][c] = 1
    while move:
        possible = True
        ny, nx, nd, cnt = move.popleft()
        for i in dd[nd]:
            x = dx[i] + nx
            y = dy[i] + ny
            if 0 <= x < M and 0 <= y < N:
                if area[y][x] == 0 and visit[y][x] == 0:
                    visit[y][x] = cnt + 1
                    move.append([y, x, 3-i, cnt+1])
                    possible = False
                    break
        if possible: # 네방향이 청소 or 벽일 때
            if area[ny+dy[dd[nd][1]]][nx+dx[dd[nd][1]]] == 1 : # 후진하는 곳이 벽이면
                break
            else:
                move.append([ny+dy[dd[nd][1]], nx+dx[dd[nd][1]] ,nd ,cnt])
            
    return cnt 

print(bfs())