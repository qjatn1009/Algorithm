from collections import deque
N, M = map(int, input().split())
bridge = [[] for _ in range(N+1)]
# N*N은 N이 최대 100,000이라 100억으로 메모리 초과
start, end, result = 1, 0, 0
for i in range(M):
    a, b, c = map(int, input().split())
    bridge[a].append((b, c))
    bridge[b].append((a, c))
    if end <= c:
        end = c
p = list(map(int, input().split()))

def bfs(weight):
    move = deque()
    move.append(p[0])
    visit = [0] * (N+1)
    while move:
        s = move.popleft()
        for i in range(len(bridge[s])):
            if bridge[s][i][1] >= weight and visit[bridge[s][i][0]] == 0:
                if bridge[s][i][0] == p[1]:
                    return True
                else:
                    move.append(bridge[s][i][0])
                    visit[bridge[s][i][0]] = 1
    return False

while start <= end:
    mid = (start + end) // 2
    if bfs(mid): # p[0] -> p[1] 가능
        result = mid
        start = mid + 1
    else:  # p[0] -> p[1] 불가능
        end = mid - 1
print(result)