N, M = map(int, input().split())
result = [1 for _ in range(M)]

def backtracking(index):
    
    if index == M:
        print(*result)
        return

    for i in range(result[index-1], N+1):
        result[index] = i
        backtracking(index + 1)

backtracking(0)