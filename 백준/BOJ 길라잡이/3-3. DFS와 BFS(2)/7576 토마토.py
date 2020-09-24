# list는 시간초과 deque는 통과
from collections import deque

M, N = map(int, input().split()) 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tomato = []
move = deque()
count = 0
for i in range(N):
    t =  list(map(int, input().split()))
    tomato.append(t)
    for j in range(M):
        if t[j] == 1:
            move.append([i,j])
        elif t[j] == 0:
            count += 1

def bfs():
    result, c = 0, 0
    while move:
        row, col = move.popleft()
        if c == count:
            return result
            break
        for i in range(4):
            x = row + dx[i]
            y = col + dy[i]
            if 0 <= x < N and 0 <= y < M:
                if tomato[x][y] == 0 :
                    tomato[x][y] = tomato[row][col] + 1
                    move.append([x,y])
                    c+= 1
                    if result < tomato[x][y]-1:
                        result = tomato[x][y]-1
    
    return -1

print(bfs())           