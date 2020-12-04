from collections import deque
dy = [-1, 1, 0, 0,]
dx = [0, 0, -1, 1]
board = []
y, x = 0, 0
baby_size, eat_count, time = 2, 0, 0
n = int(input())
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] == 9:
            y = i
            x = j

def eat_check(size): # 먹을 수 있는 물고기 확인
    for i in range(n):
        for j in range(n):
            if 0 < board[i][j] < size:
                return (False)
    return (True)

def bfs(ny, nx, time):
    check = [[0 for _ in range(n)] for _ in range(n)]
    move = deque()
    move.append([ny, nx])
    eat_fish = []
    while (move):
        ny, nx = move.popleft()
        for i in range(4):
            y = ny + dy[i]
            x = nx + dx[i]
            if 0 <= y < n and 0 <= x < n:
                if board[y][x] > baby_size: # 크기 큰 경우
                    continue
                else:
                    if check[y][x] == 0: 
                        if board[y][x] == baby_size or board[y][x] == 0: # 크기가 같거나 물고기 없는 경우
                            check[y][x] = check[ny][nx] + 1
                            move.append([y, x])
                        else: # 먹을 물고기가 있는 경우
                            check[y][x] = check[ny][nx] + 1 
                            eat_fish.append([y, x, time + check[y][x]])
    eat_fish.sort(key = lambda x :( x[2], x[0], x[1]))
    if len(eat_fish) == 0:
        return ([])
    else:
        return (eat_fish[0])


while (True):
    if eat_check(baby_size):
        print(time)
        break
    board[y][x] = 0
    possilbe = bfs(y, x, time)
    if possilbe:
        y, x, time = possilbe
    else:
        print(time)
        break
    eat_count += 1
    board[y][x] = 9
    if eat_count == baby_size:
        baby_size += 1
        eat_count = 0