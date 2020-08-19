import sys
N=int(sys.stdin.readline())
y=0
for i in range(N-len(str(N)*9),N):
    y=0
    x=0
    x+=i
    y+=i
    while(i>0):
        x+=i%10
        i=i//10
    if(x==N):
        break
    else:
        y=0
print(y)