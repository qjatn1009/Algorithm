N = int(input())
house = []
for i in range(N):
    house.append(list(map(int, input().split())))
impossible, result = 1000, 1000*1000 + 1 # 나올수 없는 최대 값

for i in range(3):
    dp = [[0 for _ in range(3)] for _ in range(N)]    
    for j in range(3):  # 처음 선택한 색만 선택되게 만듬
        if i == j :
            dp[0][j] = house[0][i]
        else:
            dp[0][j] = impossible

    for j in range(1, N): # RGB거리와 같은 방식으로 처리
        dp[j][0] = house[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = house[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = house[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if i != j:
            result = min(result, dp[N-1][j])

print(result)