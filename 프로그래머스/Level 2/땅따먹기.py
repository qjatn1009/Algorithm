# DP 문제 , 틀림
def solution(land):
    answer = 0
    current, cnt = land[0].index(max(land[0])), 0
    while cnt < len(land):

        if current == land[cnt+1].index(max(land[cnt+1])):
            if sorted(land[cnt])[-1] + sorted(land[cnt+1])[-2] > sorted(land[cnt])[-2] + sorted(land[cnt+1])[-1]:
                answer += sorted(land[cnt])[-1] + sorted(land[cnt+1])[-2]
                current = land[cnt+1].index(sorted(land[cnt+1])[-2])
                cnt += 2
            else:
                answer += sorted(land[cnt])[-2] + sorted(land[cnt+1])[-1]
                current = land[cnt+1].index(sorted(land[cnt+1])[-1])
                cnt += 2
        else:
            answer += max(land[cnt])
            current = land[cnt].index(max(land[cnt]))
            cnt += 1
        
     

    return answer

print(solution(	[[1, 2, 3, 5], [10, 11, 12, 11], [16, 15, 13, 13]]))