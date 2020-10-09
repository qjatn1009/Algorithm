def solution(skill, skill_trees):
    answer = 0
    s = len(skill)
    for skill_tree in skill_trees:
        check = [30] * s
        for j in range(s):
            if skill[j] in skill_tree:
                check[j] = skill_tree.index(skill[j])+1
        count, possible = check[0], True
        
        for j in range(1, s):
            if count > check[j]:
                possible = False
                break
            else:
                count = check[j]

        if possible:
            answer += 1
            
    return answer

skill = "ADEB"
skill_trees = ["AB"]	

print(solution(skill, skill_trees))