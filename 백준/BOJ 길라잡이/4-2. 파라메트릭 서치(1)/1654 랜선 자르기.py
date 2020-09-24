K, N = map(int, input().split())
line, total = [], 0
for i in range(K):
    line.append(int(input()))
    total += line[-1]
start, end, result = 1, total // N, 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(K):    
        cnt += line[i] // mid
    
    if cnt >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
    
print(result)