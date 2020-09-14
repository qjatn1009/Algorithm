A = int(input())
a =[0] + list(map(int, input().split()))
dp = [0] * (A+1)

for i in range(1, A+1): # 모든 수열을 하나 씩
    dp[i] = 1
    for j in range(1,i+1): # a[i] 보다 작은 수 찾기
        if a[i] > a[j]: # 작은 경우
            dp[i] = max(dp[j]+1, dp[i])
            # 1을 더한것 과 지금 값을 비교

print(max(dp[1:]))