N = int(input())
weight,height,result=[],[],[]
for i in range(N):
    x,y= map(int, input().split())
    weight.append(x)
    height.append(y)
for i in range(N):
    rank=1
    for j in range(N):
        if weight[i]<weight[j] and height[i]<height[j]:
            rank+=1
    result.append(rank)
for i in result:
    print(i,end=" ")