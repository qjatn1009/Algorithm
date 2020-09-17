def solution(routes):
    answer = 1
    road = sorted(routes)
    cctv = road[0]
    for i in range(1,len(road)):
        
        if road[i][1] <= cctv[1]: # 포함관계
            cctv = road[i]
        else: # 포함하지 않는데 1개만 벗어나거나 2개다 벗어나면
            if cctv[1] >= road[i][0]: # 1개만 벗어난 경우
                cctv = [road[i][0], cctv[1]]
            else: # 둘다 벗어 난 경우
                answer += 1
                cctv = road[i]
        
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))

print(solution([[-18,-13], [-5,-3]]))