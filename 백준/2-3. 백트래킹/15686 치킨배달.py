from itertools import combinations

N, M = map(int, input().split())
city = []
house = []
chicken = []
for i in range(N):
    city.append(list(map(int, input().split())))

for i in range(N):  #치킨집, 집을 분리
    for j in range(N):
        lists = [i, j]
        if city[i][j] == 1:
            house.append(lists)
        elif city[i][j] == 2:
            chicken.append(lists)

distance = []
for i in house:   #집에서 모든 치킨집의 거리를 구함
    houseChicken = []
    for j in chicken:
        houseChicken.append(abs(i[0]-j[0])+abs(i[1]-j[1]))
    distance.append(houseChicken)

possible = list(combinations([i for i in range(len(chicken))], M))
result = []
for i in possible:  #모든 경우의 수에서 가장 가까운 총합 거리구함
    sum = 0
    for j in distance:
        minValue = 101
        for k in range(M):
            if minValue > j[i[k]]:
                minValue = j[i[k]]
        sum += minValue
    result.append(sum)

print(min(result))