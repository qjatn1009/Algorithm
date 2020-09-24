import heapq

N = int(input())
left, right,result = [], [], [] 
for i in range(1,N+1):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, (-num, num)) # left 최대 힙
    else:
        heapq.heappush(right, (num, num)) # right 최소 힙
    
    # left 최댓값과 right 최솟값을 비교해서 
    # left 최댓값보다 right의 모든 값이 더 크게 생성
    if right and left[0][1] > right[0][1]: 
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))
    result.append(left[0][1])

for i in result:
    print(i)
