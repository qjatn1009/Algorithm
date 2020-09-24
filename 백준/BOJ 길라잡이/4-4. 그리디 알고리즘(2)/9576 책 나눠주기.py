import heapq
T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split())
    number, book = [], [0] * (N+1)
    cnt = 0

    for i in range(M):
        a, b = map(int, input().split())
        heapq.heappush(number, (b, a)) # 왜 b, a 기준이지

    for i in range(M):
        b, a = heapq.heappop(number)
        for j in range(a, b+1):
            if book[j] == 0:
                book[j] = 1
                cnt += 1
                break

    result.append(cnt)

for i in result:
    print(i)