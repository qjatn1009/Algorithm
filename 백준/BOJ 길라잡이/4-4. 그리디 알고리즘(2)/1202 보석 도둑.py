import heapq

N, K = map(int, input().split())
jew, bag = [], []
money, possible = 0, []
visit = [True for _ in range(N)]
for _ in range(N):
    w, p = map(int, input().split())
    heapq.heappush(jew, [w, p])

for _ in range(K):
    bag.append(int(input()))
bag.sort()


for i in range(K):
    weight = bag[i]
    # 가방무게보다 작은 보석을 possible로 이동
    while jew and weight >= jew[0][0]: 
        [w , p] = heapq.heappop(jew)
        heapq.heappush(possible, -p)

    if possible: # 담을 보석이 있다면
        money -= heapq.heappop(possible)
    else:
        continue
print(money)