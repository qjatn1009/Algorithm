n = int(input())
paper, result = [], [0, 0] # 종이
for i in range(n):
    line = list(map(int, input().split()))
    for j in line: # 흰색 0 파란색 1
        if j == 0:
            result[0] += 1
        else:
            result[1] += 1
    paper.append(line)

def cut(ny, nx, l, num):
    if paper[ny][nx] > l:
        return
    for y in range(l):
        for x in range(l):
            if paper[ny+y][nx+x] != num:
                return 
    for y in range(l):
        for x in range(l):
            paper[ny+y][nx+x] = l
    if num == 0 :
        result[0] -= (l**2)-1
    else:
        result[1] -= (l**2)-1

while n > 1:
    for y in range(0, len(paper), n):
        for x in range(0, len(paper), n):
            
            cut(y, x, n, paper[y][x])
    n //= 2

for i in result:
    print(i)