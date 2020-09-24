N = int(input())
card = [0] + list(map(int, input().split()))
dp = [0] *(N+1)

for i in range(1, N+1):
    for j in range(i, N+1):
        dp[j] = max(dp[j], dp[j-i]+card[i]) # 조금 헷갈림
print(dp[N])