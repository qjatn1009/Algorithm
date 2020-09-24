# 9% 탈락
from collections import deque
from math import sqrt
n, k = map(int, input().split())
dot = []
for i in range(n):
    x, y = map(int , input().split())
    dot.append([x, y])
dot.sort(key = lambda x : x[0]+x[1])
dot.append([10000, 10000])
S, T = [0, 0]
start, end, result = 1, 1415, 0

def distance(x1, y1, x2, y2): # 좌표사이 거리로 연료필요한량 리턴
    r = sqrt((x2-x1)**2+(y2-y1)**2)
    cnt = 0
    if r % 10 == 0:
        cnt = r // 10
    else:
        cnt = (r // 10)+1
    return cnt

def bfs(s):
    visit = [-1] * (n+1)
    move = deque()
    move.append([0, 0, 0])
    while move:
        x, y, z = move.popleft()
        for i in range(n+1):
            if distance(x,y,dot[i][0],dot[i][1]) <= s and visit[i] == -1:
                visit[i] = z
                move.append([dot[i][0], dot[i][1], z+1])
    return visit[-1]
while start <= end :
    mid = (start + end) // 2
    if 0 < bfs(mid) <= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)
