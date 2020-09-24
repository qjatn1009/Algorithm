from collections import deque

M, N = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 오 왼, 아래, 위
cheese = []
move_list = deque()
move = deque()
count = 0
for i in range(M):
    c = list(map(int, input().split()))
    for j in range(N):
        if c[j] == 1:
            count +=1 
    cheese.append(c)

result = [[0,count]]
def bfs(time, count): # 외부 치즈와 붙어 있는 치즈 제거
    time += 1
    while move_list:
        row, col = move_list.popleft()
        
        for i in range(4):
            x = col + dx[i]
            y = row + dy[i]
            
            if 0 <= x < N and 0 <= y < M:
                if cheese[y][x] == 1 :
                    cheese[y][x] = 0
                    count -= 1
    result.append([time, count])                                    

def check_bfs(): # 외부만 검사
    visit = [[0 for _ in range(N)] for _ in range(M)]
    move.append([0,0])
    while move:
        row, col = move.popleft()

        for i in range(4):
            x = col + dx[i]
            y = row + dy[i]
            
            if 0 <= x < N and 0 <= y < M:
                if cheese[y][x] == 0 and visit[y][x] == 0:
                    visit[y][x] = 1
                    move_list.append([y,x])
                    move.append([y,x])
    

while result[-1][1] > 0:
    check_bfs()
    bfs(result[-1][0], result[-1][1])

print(result[-1][0])
print(result[-2][1])