T = int(input())
result = []
for i in range(T):
    n = int(input())
    student = [0] + list(map(int, input().split()))
    visit = [0] * (n+1)
    group = 1

    for j in range(1,n+1):
        if visit[j] == 0:
            while visit[j] == 0:  # 사이클 생성
                visit[j] = group
                j = student[j]
            while visit[j] == group: # 사이클 검사
                visit[j] = -1 
                j = student[j]
            group += 1

    for k in visit:
        if k < 0:
            n -= 1
    result.append(n)

for i in result:
    print(i)