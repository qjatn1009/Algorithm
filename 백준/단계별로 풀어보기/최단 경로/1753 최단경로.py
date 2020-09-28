import heapq
import sys
input = sys.stdin.readline
INF = int(10e9)

V, E = map(int, input().split())

start = int(input())
lines = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    lines[u].append([v, w])

def diijkstra(start):
    q = [ ]
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in lines[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]: # 값을 비교
                distance[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))

diijkstra(start)

for i in range(1, V+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INF")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])