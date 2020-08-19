N,M = map(int,input().split())
result=[]
chessboard1= ["WBWBWBWB","BWBWBWBW"]*4
chessboard2= ["BWBWBWBW","WBWBWBWB"]*4
board=[]
for row in range(N):
    board_row=input()
    board.append(board_row)
compare=chessboard1
for k in range(2):
    for row in range(N-7):
        for column in range(M-7):
            count=0
            for i in range(8):
                for j in range(8):
                    if board[i+row][j+column]!=compare[i][j]:
                        count+=1
            result.append(count)
    compare = chessboard2
print(min(result))