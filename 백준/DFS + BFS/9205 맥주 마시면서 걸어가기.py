from collections import deque
T = int(input())
result = []
for _ in range(T):
    n = int(input())
    start = list(map(int, input().split()))
    store = []
    for _ in range(n):
        store.append(list(map(int, input().split())))
    end = list(map(int, input().split()))
    store.sort(key = lambda x : x[0]+x[1])

    def bfs():
        move = deque()
        move.append(start)
        visit = [0] * n
        while move:
            x, y = move.popleft()
            if abs(end[0]-x) + abs(end[1]-y) <= 1000:
                return True
            for i in range(n):
                if abs(store[i][0] - x)+ abs(store[i][1] - y) <= 1000 and visit[i] == 0:
                    visit[i] = 1
                    move.append([store[i][0], store[i][1]])
        return False

    if bfs():
        result.append("happy")
    else:
        result.append("sad")
for i in result:
    print(i)