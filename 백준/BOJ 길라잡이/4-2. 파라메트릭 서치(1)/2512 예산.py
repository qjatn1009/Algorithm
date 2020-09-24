N = int(input())
budget = list(map(int, input().split()))
M = int(input())
start, end, result = 1, max(budget), 0

while start <= end:
    mid = (start + end) // 2
    money = 0
    for i in range(N):
        if budget[i] <= mid:
            money += budget[i]
        else:
            money += mid
    if money == M:
        result = mid
        break
    elif money < M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(result)