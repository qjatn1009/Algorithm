n, m, y, x, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
command = list(map(int, input().split()))
dice = [0 for i in range(7)]
result = []
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

def turn_dice(turn): # 주사위 굴리기
    if turn == 1:
        change = [3, 2, 6, 1, 5, 4]
    elif turn == 2:
        change = [4, 2, 1, 6, 5, 3]
    elif turn == 3:
        change = [2, 6, 3, 4, 1, 5]
    else:
        change = [5, 1, 3, 4, 6, 2]
    change_dice = [0]
    for i in change:
        change_dice.append(dice[i])
    return change_dice

def check(y, x, turn):
    ny = y + dy[turn]
    nx = x + dx[turn]
    if 0 <= ny < n and 0 <= nx < m:
        return ny, nx, True
    else:
        return y, x, False

for i in range(k):
    y, x, possible = check(y, x, command[i])
    if possible:
        dice = turn_dice(command[i])
        if board[y][x] == 0:
            board[y][x] = dice[6]
        else:
            dice[6] = board[y][x]
            board[y][x] = 0
        result.append(dice[1])
    else:
        continue

for i in result:
    print(i)