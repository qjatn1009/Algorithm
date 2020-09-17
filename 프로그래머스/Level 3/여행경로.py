def solution(tickets):
    answer = []
    visit = [True] * len(tickets)
    route = ["ICN"]
    def dfs(route, index):
        if index == len(tickets):
            result = []
            for i in route:
                result.append(i)
            answer.append(result)
            return 
        for i in range(len(tickets)):
            if tickets[i][0] == route[-1] and visit[i]:
                route.append(tickets[i][1])
                visit[i] = False
                dfs(route, index+1)
                route.pop()
                visit[i] = True
    dfs(route, 0)
    
    answer.sort()

    return answer[0]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))