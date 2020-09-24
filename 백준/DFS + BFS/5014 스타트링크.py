from collections import deque
F, S, G, U, D = map(int, input().split())
# F : 전체 층수
# S : 현재 층수
# G : 목적지 층수
# U : 위버튼 마다 올라가는 수
# D : 다운버튼 마다 내려가는 수

def bfs():
    visit = [0] * (F+1)
    move = deque()
    move.append([S, 0])
    while move:
        now, cnt = move.popleft()
        if now == G:
            return cnt
        up, down = now + U, now - D
        if 0 < up <= F and visit[up] == 0:
            visit[up] = 1
            move.append([up, cnt+1])
        if 0 < down <= F and visit[down] == 0:
            visit[down] = 1
            move.append([down, cnt+1])

    return "use the stairs"

print(bfs())