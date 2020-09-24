import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        return answer
    else:
        while True:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, b*2 + a)
            answer += 1
            if scoville[0] >= K:
                break
            if len(scoville) == 1:
                answer = -1
                break
    return answer


print(solution([12, 10, 9, 3, 2, 1], 7))