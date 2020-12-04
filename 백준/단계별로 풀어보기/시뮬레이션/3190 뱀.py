from collections import deque

n = int(input())
k = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
for i in range(k):
    a_y, a_x = list(map(int, input().split()))
    board[a_y - 1][a_x - 1] = 1
L = int(input())
move = deque()
for i in range(L):
    data = list(input().split())
    move.append([int(data[0]), data[1]])

# L : 왼쪽 D : 오른쪽
# 동 0 : L = 북 3 , R = 남 2
# 서 1 : L = 남 2 , R = 북 3
# 남 2 : L = 동 0 , R = 서 1
# 북 3 : L = 서 1 , R = 동 0
time = 0
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
snake_dir = 0
snake = deque()
snake.append([0, 0])
board[0][0] = 2
def change(direction, turn):
    if turn == "L":
        arr = [3, 2, 0, 1]
    else:
        arr = [2, 3, 1, 0]
    return (arr[direction])

while True:
    ny, nx = snake[0]
    y, x = ny + dy[snake_dir], nx + dx[snake_dir]
    
    if 0 <= y < n and 0 <= x < n:
        if board[y][x] == 2: # 자기 몸과 부딪힘
            print(time + 1)
            break
        elif board[y][x] == 1: # 사과 O
            snake.appendleft([y, x])
            board[y][x] = 2
        else: # 사과 X
            board[y][x] = 2
            snake.appendleft([y, x])
            tail = snake.pop()
            board[tail[0]][tail[1]] = 0
    else: # 벽에 부딪힘
        print(time + 1)
        break
    time += 1
    if len(move) != 0:
        if time == move[0][0]:
            times, turn = move.popleft()
            snake_dir = change(snake_dir, turn)