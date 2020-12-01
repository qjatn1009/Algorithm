now = input()
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]
move = [0, int(now[1])]
result = 0
for i in range(8):
    if row[i] == now[0]:
        move[0] = i + 1
        break
dy = [-2, -2, 2, 2, 1, -1, 1, -1]
dx = [-1, 1, -1, 1, 2, 2, -2, -2]
# l r u d
for i in range(8):
    x = move[0] + dx[i]
    y = move[1] + dy[i]
    if 1 <= x <= 8 and 1 <= y <= 8:
        result += 1
print(result)