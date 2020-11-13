def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        if not dic.get(genres[i]):
            dic[genres[i]] = [plays[i],[plays[i], i]]
        else:
            dic[genres[i]].append([plays[i], i])
            dic[genres[i]][0] += plays[i]
    for i in dic:
        dic[i][1:] = sorted(dic[i][1:], reverse= True, key = lambda x : x[0])
    print(dic)
    dic = sorted(dic.items(), key = lambda x : x[1][0], reverse= True)
    print(dic)
    for i in dic:
        if len(i[1]) >= 3:
            answer.append(i[1][1][1])
            answer.append(i[1][2][1])
        else:
            answer.append(i[1][1][1])
    return answer

# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["a","b","a","b","c"], [100,200,300,400,500]))