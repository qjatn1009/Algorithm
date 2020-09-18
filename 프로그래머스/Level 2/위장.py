def solution(clothes):
    answer = 0
    dic = {}
    for value, key in clothes:
        if not dic.get(key):
            dic[key] = [value]
        else:
            dic[key].append(value)
    if len(dic) == 1:
        answer = len(clothes)
    else:
        num = 1
        for i in dic:
            num *= len(dic[i]) + 1
        answer = num - 1
    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))