import heapq

N = int(input())
card, result = [], 0
for i in range(N):
    heapq.heappush(card, int(input()))

for i in range(N-1):
    result += heapq.heappop(card)
    result += heapq.heappop(card)
    
