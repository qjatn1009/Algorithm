T = int(input())
result = []
for i in range(T):
    n = int(input())
    dp = [0] * (n+1)
    if n == 1:
        dp[n] = 1
    elif n == 2:
        dp[n] = 2
    else:
        dp[1], dp[2], dp[3] = 1, 2, 4
        for j in range(4, n+1):
            for k in range(1, 4):
                dp[j] += dp[j-k]
    result.append(dp[n])
for i in result:
    print(i)