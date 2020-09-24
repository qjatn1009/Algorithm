N = int(input())
M = int(input())
virus = [[0 for _ in range(N+1)] for _ in range(N+1) ]
for i in range(M):
    row, col = map(int, input().split())
    virus[row][col] = 1
    virus[col][row] = 1
check = [False] * (N+1)
check[1] = True
count = 0 
computer = [1]
while computer:
    index = computer.pop(0)
    for i,j in enumerate(virus[index]):
        if j == 1 and not check[i]:
            computer.append(i)
            check[i] = True
            count += 1
print(count)