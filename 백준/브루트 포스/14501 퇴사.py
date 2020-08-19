# 아직 해결 못함
N = int(input())
date, money, result, day=[0],[0],0,1
for i in range(N):
    T,P = map(int, input().split())
    date.append(T)
    money.append(P)
print(date,money)

while day<=N:
    if money[day]/date[day]>=money[day+1]/date[day+1]:
        result+=money[day]
        day+=date[day]

    else:
        day+=1

print(result)
