N, C = map(int, input().split())
house = []
for i in range(N):
    house.append(int(input()))
house.sort()
start, end, result = 1, (house[-1] - house[0]) // (C - 1), 0

while start <= end:
    mid = (start + end) // 2
    router, cnt = house[0], 1
    for i in range(1, N):
        if house[i] >= router + mid:
            router = house[i]
            cnt += 1
    if cnt < C:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    
print(result)