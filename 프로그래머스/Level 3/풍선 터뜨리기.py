def solution(a):
    answer = 0
    if len(a) <= 2:
        answer = len(a)
    else:
        start, end = a[0], a[-1]
        count = [0] * len(a)
        
        for i in range(len(a)):  # 왼쪽에 작은 수 검사
            if i == 0 or i == len(a)-1 :
                continue
            else:
                if a[i] > start:
                    count[i] += 1
                else:
                   start = a[i]
        for i in range(len(a)-1, -1, -1): # 오른쪽 작은 수 검사
            if i == 0 or i == len(a)-1 :
                continue
            else:
                if a[i] > end:
                    count[i] += 1
                else:
                    end = a[i]
        answer = len(a) - count.count(2)
    return answer

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))