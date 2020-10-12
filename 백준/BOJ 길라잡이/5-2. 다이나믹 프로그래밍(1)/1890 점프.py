N = int(input())
board = []

for i in range(N):
    board.append(list(map(int, input().split())))

dp = [[0 for i in range(N)] for i in range(N)]
dp[0][0] = 1

for y in range(N):
    for x in range(N):
        if y == N-1 and x == N-1:
            break
        value = board[y][x]
        down = y + value
        right = x + value

        if down < N:
            dp[down][x] += dp[y][x] 

        if right < N:
            dp[y][right] += dp[y][x]

print(dp[-1][-1])