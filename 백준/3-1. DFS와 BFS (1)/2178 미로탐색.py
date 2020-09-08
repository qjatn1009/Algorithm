#BFS로 푼거
N, M = map(int, input().split())
miro = []
check = [[0 for i in range(M)] for _ in range(N)] 
check[0][0] = 1
move_list =[[0,0]]
for i in range(N):
    miro.append(list(map(int, input())))

def DFS(row, col):
    while move_list:
        row, col = move_list.pop(0)
        if row == N - 1 and col == M - 1 :
            print(check[row][col])
            break
        if row < N-1 and miro[row+1][col] == 1 and check[row+1][col] == 0:#아래
            check[row+1][col] = check[row][col] + 1
            move_list.append([row+1, col])
        if row > 0 and miro[row-1][col] == 1 and check[row-1][col] == 0:# 위 
            check[row-1][col] = check[row][col] + 1
            move_list.append([row-1, col])
        if col < M-1 and miro[row][col+1] == 1 and check[row][col+1] == 0:# 오른쪽
            check[row][col+1] = check[row][col] + 1
            move_list.append([row, col+1])
        if col > 0 and miro[row][col-1] == 1 and check[row][col-1] == 0:# 왼쪽
            check[row][col-1] = check[row][col] + 1
            move_list.append([row, col-1])
DFS(0, 0)


# DFS로 푼거
# 최단을 뽑기는 모든 경우의수를 해야되서 오래 걸림
# N, M = map(int, input().split())
# miro = []
# check = [[0 for i in range(M)] for _ in range(N)] 
# check[0][0] = 1
# move_list =[]
# for i in range(N):
#     miro.append(list(map(int, input())))

# def DFS(row, col):
#     if row == N-1 and col == M-1:
#         move_list.append(check[row][col])
#         return
#     else:
#         if row < N-1 and miro[row+1][col] == 1 and check[row+1][col] == 0:#아래
#             check[row+1][col] = check[row][col] + 1
#             DFS(row+1, col)
#             check[row+1][col] = 0
#         if row > 0 and miro[row-1][col] == 1 and check[row-1][col] == 0:# 위 
#             check[row-1][col] = check[row][col] + 1
#             DFS(row-1, col)
#             check[row-1][col] = 0
#         if col < M-1 and miro[row][col+1] == 1 and check[row][col+1] == 0:# 오른쪽
#             check[row][col+1] = check[row][col] + 1
#             DFS(row, col+1)
#             check[row][col+1] = 0
#         if col > 0 and miro[row][col-1] == 1 and check[row][col-1] == 0:# 왼쪽
#             check[row][col-1] = check[row][col] + 1
#             DFS(row, col-1)
#             check[row][col-1] = 0
# DFS(0, 0)
# print(min(move_list))