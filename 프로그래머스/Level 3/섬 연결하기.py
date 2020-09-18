def solution(n, costs):
    answer = 0
    costs.sort(key= lambda x : x[2])
    visit = [[0 for i in range(n) ] for i in range(n)]
    for i in range(n):
        visit[i][i] = 1
    for island1, island2, cost in costs:
        link = []
        if visit[island1][island2] == 0 and visit[island2][island1] == 0:
            visit[island1][island2] = 1
            visit[island2][island1] = 1
            for j in range(n):
                if visit[island1][j] == 1 or visit[island2][j] == 1:
                    link.append(j)
            for j in link:
                for k in link:
                    visit[j][k] = 1
            answer += cost
    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(5, [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]]))