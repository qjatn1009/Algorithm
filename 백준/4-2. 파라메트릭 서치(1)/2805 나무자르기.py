N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

start, end, result = 0, tree[-1], 0

while start <= end:
    mid = (start + end) // 2
    height = 0
    for i in tree:
        if i <= mid:
            continue
        else:
            height += i - mid
    if height == M:
        result = mid
        break
    elif height > M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)