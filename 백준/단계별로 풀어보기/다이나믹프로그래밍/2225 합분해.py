n, k = map(int, input().split())
dp = [[1 for _ in range(n+1)] for _ in range(k+1)]
if k == 1:
    dp[1] = [1 for _ in range(n+1)]
elif k == 2:
    dp[2] = [i+1 for i in range(n+1)] 
else:
    dp[1] = [1 for _ in range(n+1)]
    dp[2] = [i+1 for i in range(n+1)]

    for i in range(3, k+1):
        dp[i][1] = i
        for j in range(2,n+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[k][n])