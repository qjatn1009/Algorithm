N = int(input())
house = []
for i in range(N):
    house.append(list(map(int, input().split())))

def solve(index):
    for i in range(1,index):
        for j in range(3):
            if j == 0:
                house[i][j] += min(house[i-1][1], house[i-1][2])
            elif j == 1:
                house[i][j] += min(house[i-1][0], house[i-1][2])
            else:
                house[i][j] += min(house[i-1][0], house[i-1][1])
    return min(house[i])

print(solve(N))