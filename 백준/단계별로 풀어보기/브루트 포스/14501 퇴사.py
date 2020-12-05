N = int(input())
day = [[0, 0]]
dp = [0] * (N + 1)
for i in range(N):
    day.append(list(map(int, input().split())))
    day[i + 1][0] += i

for i in range(1, N + 1):
    dp[i] = dp[i- 1]
    for j in range(1, i + 1):
        if i == day[j][0]:
            dp[i] = max(dp[j - 1] + day[j][1], dp[i])
print(dp[-1])