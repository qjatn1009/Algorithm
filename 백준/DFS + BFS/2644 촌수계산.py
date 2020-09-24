from collections import deque
n = int(input())
a, b = map(int, input().split())
m = int(input())
p = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    p[x][y] = 1
    p[y][x] = 1
    
def bfs():
    visit = [0] * (n+1)
    visit[a] = 1
    r = deque()
    r.append([a, 0])
    while r:
        p1, cnt = r.popleft()
        for i in range(n+1):
            if p[p1][i] == 1 and visit[i] == 0:
                if i == b:
                    return cnt+1
                else:
                    visit[i] = 1
                    r.append([i, cnt+1])
    return -1

print(bfs())