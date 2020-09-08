N = int(input())
stairs = []
for i in range(N):
    stairs.append(int(input()))
score = 0
# 한 단계 or 두 단계 상승 가능
# 연속 세 계단 이상 밟으면 안됨
# 최고의 점수 합을 출력
move_list = []
def dp(index):
    print(index)
    global score
    if index == 0:
        return stairs[index]
    else:
        return max(stairs[index]+stairs[index-1]+dp(index-3), stairs[index]+stairs[index-2])
print(dp(N-1))
# print(score)
