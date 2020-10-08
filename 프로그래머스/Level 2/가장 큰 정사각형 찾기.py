# DP 문제
def solution(board): # 전체 검사하면 무조건 시간 초과
    answer = 0
    ny, nx = len(board), len(board[0])
    for y in range(ny):
        for x in range(nx):
            if board[y][x] == 1:
                answer = 1
    for y in range(1, ny):
        for x in range(1, nx):
            if board[y][x] == 0:
                continue
            else:
                if board[y-1][x]*board[y-1][x-1]*board[y][x-1] >0 : 
                    board[y][x] = min(board[y-1][x], board[y-1][x-1], board[y][x-1]) + 1
                    if answer < board[y][x]:
                        answer = board[y][x]
    answer *= answer
    return answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))