from copy import deepcopy
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
#위 반시계 방향
board = [[] for _ in range(4)]
y, x = 0, 0
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(0, 8, 2):
        board[i].append(data[j:j+2])

get_fish = []

# 번호 작은 물고기 부터 이동
# 이동 O : 빈칸, 다른 물고기
# 이동 X : 상어, 공간의 경계를 넘는 칸

def find_fish(index, arr): # 물고기 번호 찾기
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == index:
                return (i, j)
    return None

def change_fish(arr): # 물고기 이동
    position = []
    for i in range(1, 17):
        position = find_fish(i, arr)
        if position is None:
            continue
        y, x = position
        direction = arr[y][x][1]
        for j in range(8):
            if direction > 8:
                direction %= 8
            ny, nx = y + dy[direction], x + dx[direction]
            if 0 <= ny < 4 and 0 <= nx < 4:
                if arr[ny][nx][0] != 'S':
                    arr[y][x][1] = direction
                    arr[ny][nx], arr[y][x] = arr[y][x], arr[ny][nx]
                    break
            direction += 1
    

def check_board(y, x, arr): # 가능한 물고기 찾기
    d = arr[y][x][1]
    while True:
        y, x = y + dy[d], x + dx[d]
        if 0 <= y < 4 and 0 <= x < 4:
            if arr[y][x][0] > 0 :
                return (False) 
        else:
            return (True)

def dfs(y, x, num, board):
    arr = deepcopy(board)
    num += arr[y][x][0]
    arr[y][x][0] = 'S'
    change_fish(arr)

    if check_board(y, x, arr):
        get_fish.append(num)
        return 
    for i in range(1, 4):
        d = arr[y][x][1]
        ny, nx = y + (dy[d] * i), x + (dx[d] * i)
        if 0 <= ny < 4 and 0 <= nx < 4 and arr[ny][nx][0] != 0:
            dire = arr[y][x][1]
            arr[y][x] = [0, 0]
            dfs(ny, nx, num, arr)
            arr[y][x][1] = dire

dfs(y, x, 0, board)
print(max(get_fish))