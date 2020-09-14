from collections import deque

M, N, K = map(int, input().split())
paper = [[0 for i in range(N)] for i in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 오 왼, 아래, 위
result, cnt = [], 0
for i in range(K):
    sqare = list(map(int, input().split()))
    for j in range(sqare[0], sqare[2]):
        for k in range(sqare[1], sqare[3]):
            paper[k][j] = 1

def bfs(row, col):  # 영역을 bfs로 구함
    area = 1
    move = deque()
    move.append([row, col])
    while move:
        row, col = move.popleft()

        for i in range(4):
            x = col + dx[i]
            y = row + dy[i]
            
            if 0 <= x < N and 0 <= y < M:
                if paper[y][x] == 0:
                    paper[y][x] = 1
                    area += 1
                    move.append([y,x])
    return area

for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            paper[i][j] = 1
            result.append(bfs(i,j))
            cnt += 1
print(cnt)
result.sort()
print(*result)