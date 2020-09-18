def solution(n, money):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = 1
    for i in money:
        for j in range(i, n+1):
            dp[j] += dp[j-i]
    answer = dp[-1]
    return answer

print(solution(5, [1, 2, 5]))