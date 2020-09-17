def solution(begin, target, words):
    answer = 0
    result = []
    if target not in words:
        pass
        return answer
    else:
        visited = [0] * len(words)
        def dfs(word, count):
            if word == target:
                result.append(count)
                return
            for i in range(len(words)):
                cnt = 0
                if visited[i] == 0:
                    for j in range(len(words[i])):
                        if cnt > 1:
                            break
                        else:
                            if word[j] != words[i][j] :
                                cnt += 1  
                    
                    if cnt <= 1:
                        visited[i] = 1
                        dfs(words[i], count+1)
                        visited[i] = 0
        dfs(begin, 0)
        answer = min(result)     
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
