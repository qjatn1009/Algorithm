n = int(input())
store = list(map(int, input().split()))
m = int(input())
customer = list(map(int, input().split()))
store.sort()
result = []
for i in range(m):
    target = customer[i]
    start, end = 0, n - 1
    while (start <= end):
        mid = (start + end) // 2
        if store[mid] == target:
            result.append("yes")
            break
        elif store[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if len(result) != i + 1:
        result.append("no")

print(*result)