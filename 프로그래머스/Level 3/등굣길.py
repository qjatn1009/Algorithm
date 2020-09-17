def solution(m, n, puddles):
    answer = 0
    check = [[0 for _ in range(m)] for _ in range(n)]
    road = [[0 for _ in range(m)] for _ in range(n)]
    check[0][0] = 1
    for i in puddles:
        road[i[1]-1][i[0]-1] = 1
    for i in range(n):
        for j in range(m):
            if road[i][j] == 1 :
                continue
            else:
                check[i][j] += check[i-1][j] + check[i][j-1]

    answer = check[n-1][m-1] % 1000000007
        
    return answer


print(solution(4, 3, [[2, 2]]))