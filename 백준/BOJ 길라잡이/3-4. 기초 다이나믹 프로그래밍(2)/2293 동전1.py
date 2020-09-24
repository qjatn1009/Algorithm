n, k = map(int, input().split())
coin = []
dp = [0]*(k+1)
dp[0] = 1
for i in range(n):
    coin.append(int(input()))

for i in coin: #동전을 순회
    for j in range(1,k+1): # 가치를 순회
        if j - i >= 0:
            dp[j] += dp[j-i] 
print(dp[k])