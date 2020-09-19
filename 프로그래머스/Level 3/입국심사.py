def solution(n, times):
    answer = 0
    start, end= 1, max(times) * (n // len(times))
    # 시간 / 심사시간 = 입국자 맡는 인원 수
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(len(times)):
            cnt += mid // times[i]
        
        if cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

print(solution(6, [7, 10]))