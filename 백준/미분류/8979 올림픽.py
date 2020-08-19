import sys   #백준 8979번 올림픽
n,k=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    line=sys.stdin.readline().split()
    line=list(map(int,line))
    arr.append(line)
arr.sort(reverse=True,key=lambda x:(x[1],x[2],x[3]))  #금.은.동 순서로 정렬
m=0
medal=[0,0,0]
for i in range(n):  #획득한 메달이 같은 국가끼리는 같은 등수로 취급
    m+=1
    if medal!=arr[i][1:]:
        medal=arr[i][1:]
        arr[i].append(m)
    else:
        arr[i].append(arr[i-1][4])
    if(arr[i][0]==k):
        result=arr[i][4]
        break
print(result)