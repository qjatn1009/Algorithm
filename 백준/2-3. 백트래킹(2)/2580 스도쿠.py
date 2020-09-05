# 개어렵다
sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
count = 0
def horizontal(x, val): # 가로 검사
    if val in sudoku[x]:
        return False
    return True

def vertical(y, val): # 세로 검사
    for i in range(9):
        if val == sudoku[i][y]:
            return False
    return True

def square(x, y, val): # 3x3 검사
    nx = (x // 3) * 3
    ny = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[nx+i][ny+j]:
                return False
    return True

def DFS(index):
    global count
    if index == len(zeros):
        for rows in sudoku:
            print(*rows)
        exit(0)

    else:
        for i in range(1, 10):
            nx = zeros[index][0]
            ny = zeros[index][1]
            
            if horizontal(nx, i) and vertical(ny, i) and square(nx, ny, i):
                sudoku[nx][ny] = i
                DFS(index+1)
                sudoku[nx][ny] = 0

DFS(0)