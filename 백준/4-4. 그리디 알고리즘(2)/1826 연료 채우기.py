import sys
import heapq
def input(): return sys.stdin.readline()

N = int(input())
station = []
for i in range(N):
    a, b = map(int, input().split())
    heapq.heappush(station, (a, b))
L, R = map(int, input().split())
cnt, now = 0, R
q = []
while True:
    if now >= L : # 갈 수 있는 최대 거리
        break
    
    else:
        while(station): 
            a, b = heapq.heappop(station) 
            if a <= now : # 갈 수 있는 주유소
                heapq.heappush(q, -b)
            else: # 갈 수 없는 주유소
                heapq.heappush(station, (a, b))
                break
        
        if q : # 가장 기름을 많이 넣을 수 있는 곳 부터 감
            b = heapq.heappop(q)
            cnt += 1
            now -= b
        else: # 모든 주유소를 다 가도 마을 도착을 못하는 경우
            cnt = -1
            break
print(cnt)