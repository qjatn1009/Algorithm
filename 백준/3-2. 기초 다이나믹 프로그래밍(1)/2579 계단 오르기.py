# 한번 다시 볼것
N = int(input())
stairs = []
for i in range(N):
    stairs.append(int(input()))

def climb(index):
    if index < 3: 
        return sum(stairs)
    else:
        dp = [stairs[0], stairs[0]+stairs[1]]
        for i in range(2,3):
            dp.append(max(dp[i-2]+stairs[i], stairs[i-1]+stairs[i])) # 세 번째 계단 최고 점수
        
        for i in range(3, index):
            dp.append(max(stairs[i]+stairs[i-1]+ dp[i-3],stairs[i]+ dp[i-2])) # 네 번째 계단 이후 최고 점수
        
        return dp[-1]

print(climb(N))