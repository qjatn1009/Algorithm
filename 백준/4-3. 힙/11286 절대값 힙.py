import heapq

N = int(input())
result, xlist = [], []
for i in range(N):
    x = int(input())
    
    if x == 0 :
        if len(xlist) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(xlist)[1])
    elif x > 0 :
        heapq.heappush(xlist, (x, x))
    else:
        heapq.heappush(xlist, ((-x)-0.1, x))
for i in result:
    print(i)

# 밑에 코드가 더 맞는 방식

# import sys   
# import heapq

# numbers = int(input())
# heap = []

# for _ in range(numbers):
#     num = int(sys.stdin.readline())
#     if num != 0:
#         heapq.heappush(heap, (abs(num), num))
#     else:
#         try:
#             print(heapq.heappop(heap)[1])
#         except:
#             print(0)