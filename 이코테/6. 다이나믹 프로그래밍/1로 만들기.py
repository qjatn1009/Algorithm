x = int(input())
dp = [ i - 1 for i in range(x + 1)]
for i in range(1, x + 1):
    if i * 5 < x + 1 :
        dp[i * 5] = min(dp[i * 5], dp[i] + 1)
    if i * 3 < x + 1:
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    if i * 2 < x + 1:
        dp[i * 2] = min(dp[i * 2 ], dp[i] + 1)
    if i + 1 < x + 1:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)

print(dp[x])