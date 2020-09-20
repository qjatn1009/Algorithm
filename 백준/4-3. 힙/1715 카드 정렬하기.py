import heapq

N = int(input())
card, result = [], 0
for i in range(N):
    heapq.heappush(card, int(input()))
if len(card) == 1: # 카드가 한장이면 비교 횟수 0
    print(result)
else:
    for i in range(N-1): # 그 외
        count = 0
        count += heapq.heappop(card)
        count += heapq.heappop(card) # 카드 2장을 합침
        result += count # 총 횟수에 추가
        heapq.heappush(card, count) # 카드 2장합친 수 push
    print(result)