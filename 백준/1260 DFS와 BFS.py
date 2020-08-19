n, m, v = map(int, input().split())     # 백준 1260번 DFS와BFS
arr = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1
def dfs(current_node,foot_prints): # current_node : 시작점 , food_prints : 결과물
    foot_prints+=[current_node]
    for search_node in range(len(arr[current_node])):
        if arr[current_node][search_node] and search_node not in foot_prints:
            foot_prints=dfs(search_node,foot_prints)
    return foot_prints
def bfs(start):
    queue = [start]
    foot_prints=[start]
    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(arr[current_node])):
            if arr[current_node][search_node] and search_node not in foot_prints:
                foot_prints+=[search_node]
                queue +=[search_node]
    return foot_prints
print(*dfs(v,[]))
print(*bfs(v))