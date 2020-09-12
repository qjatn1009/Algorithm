# 개어려움...
N, M = map(int, input().split())
m = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    m.append(list(map(int, input())))

check = [[[0,0] for i in range(M)] for _ in range(N)] 
check[0][0][0] = 1
move_list = [[0, 0, 0]]
# check[a][b][c]에서 c가 0은 벽을 안뚫음, 1은 뚫음

def BFS():
    while move_list:
        row, col, w = move_list.pop(0)
        if row == N - 1 and col == M - 1:
            return check[row][col][w]

        for i in range(4):
            x = row + dx[i]
            y = col + dy[i]
            
            if 0 <= x < N and  0 <= y < M :
                if m[x][y] == 0 and check[x][y][w] == 0:   # w을 통해서 뚫은 것과 안 뚫은 거 나뉨
                    check[x][y][w] = check[row][col][w] + 1
                    move_list.append([x,y,w])
                elif m[x][y] == 1 and w == 0:   # 벽을 만났을 경우 벽을 뚫을 수 있는지 확인
                    check[x][y][1] = check[row][col][0] + 1  # 벽을 뚫고 [0]에서 [1]로 이동하여 뚫은 표시
                    move_list.append([x,y,1])

    return -1

print(BFS())