import sys
input = sys.stdin.readline

N = int(input())
day = [[0, 0]]
dp = [0] * (N + 1)
for i in range(N):
    day.append(list(map(int, input().strip().split())))
    day[i + 1][0] += i

for i in range(1, N + 1):
    if day[i][0] <= N:
        dp[day[i][0]] = max(dp[day[i][0]] , dp[i - 1] + day[i][1])
        # 그 날 vs 그 전날 + 오늘 완료 한 일
    dp[i] = max(dp[i - 1], dp[i])

print(dp[-1])