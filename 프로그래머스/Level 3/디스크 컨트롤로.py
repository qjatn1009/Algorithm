import heapq
def solution(jobs):
    heapq.heapify(jobs)
    answer, cnt = jobs[0][1], len(jobs)
    q, end = [], sum(heapq.heappop(jobs))
    if len(jobs) == 0:
        return answer
    while True:
        while jobs and jobs[0][0] < end:
            s, t = heapq.heappop(jobs)
            heapq.heappush(q, (t, s))
        if q :
            t, s = heapq.heappop(q)
            answer += t + end - s
            end = t + end
        else:
            answer += jobs[0][1]            
            end = sum(heapq.heappop(jobs))
        if len(jobs) == 0 and len(q) == 0:
            break
    return answer // cnt 

print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))