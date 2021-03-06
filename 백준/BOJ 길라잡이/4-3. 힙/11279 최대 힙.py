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
        heapq.heappush(xlist, (-x, x))

for i in result:
    print(i)