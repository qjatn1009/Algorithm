n = int(input())
nx, ny = 1, 1
move = list(input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# L R U D
for i in move:
    index = 0
    if i == 'L':
        index = 0
    elif i == 'R':
        index = 1
    elif i == 'U':
        index = 2
    else:
        index = 3
    y = ny + dy[index]
    x = nx + dx[index]
    if 1 <= x <= n and 1 <= y <= n:
        nx, ny = x, y

print(ny, nx)