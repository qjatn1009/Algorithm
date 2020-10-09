n, m = map(int, input().split())
judge = []
for i in range(n):
    judge.append(int(input()))
judge.sort()
start, end, time = 0, judge[-1]*m, 0

while start <= end:
    mid = ( start + end ) // 2
    count = 0
    for i in range(n):
        count += mid // judge[i]

    if count < m:
        start = mid + 1
    else:
        end = mid - 1
        time = mid

print(time)