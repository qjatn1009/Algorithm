n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))
if n == 1:
    dp = [wine[0], wine[1]]
else:
    dp = [wine[0], wine[1], 
        wine[1]+wine[2]]

for i in range(3, n+1):
    if i == 3:
        dp.append(max(wine[2]+wine[3], dp[2], wine[1]+wine[3]))
    else:
        dp.append(
        max(dp[i-4] + wine[i-2]+wine[i-1],
            dp[i-3]+wine[i]+wine[i-1],
            dp[i-2]+wine[i]))
        # 1,2와 2,3 과 3중 큰거를 선택
print(dp[n])