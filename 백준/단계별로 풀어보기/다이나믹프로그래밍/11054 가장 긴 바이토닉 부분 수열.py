N = int(input())
A = [0] + list(map(int, input().split()))
dp1 = [0] * (N+1)
dp2 = [0] * (N+1)
for i in range(1, N+1): # 모든 수열을 하나 씩
    dp1[i] = 1
    for j in range(1,i+1): # a[i] 보다 작은 수 찾기
        if A[i] > A[j]: # 작은 경우
            dp1[i] = max(dp1[j]+1, dp1[i])
            # 1을 더한것 과 지금 값을 비교

for i in range(N, 0, -1): # 위를 거꾸로
    dp2[i] = 1
    for j in range(N,i, -1): 
        if A[i] > A[j]: 
            dp2[i] = max(dp2[j]+1, dp2[i])
            

result = 0
for i in range(1, N+1):
    if result < dp1[i] + dp2[i] - 1:
        result = dp1[i] + dp2[i] - 1

print(result)