# 효율성 문제
def solution(board):
    answer = [0]
    possible = False
    m = min(len(board), len(board[0]))
    result = [ i for i in range(m,0,-1)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for k in result:
                    if k + i <= len(board) and k + j <= len(board[i]):
                        if square(i, j, k, board):
                            answer.append(k*k)
                            result = result[:result.index(k)]
                            break
    print(answer)
    return max(answer)

def square(row, column, N, board):
    for i in range(N):
        for j in range(N):
            if board[row+i][column+j] != 1:
                return False
    return True


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))