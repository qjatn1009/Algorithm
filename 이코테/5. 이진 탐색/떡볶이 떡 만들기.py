n, m = map(int, input().split())
length = list(map(int, input().split()))
length.sort()
start, end, result = 0, length[-1], 0

while (start <= end):
    count = 0
    mid = (start + end) // 2
    for i in range(n):
        if mid > length[i]:
            continue
        else:
            count += length[i] - mid
    if count >= m :
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)