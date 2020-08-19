T = int(input()) #테이스케이스 수
result = []
for i in range(T):
    cnt = 0
    N, M = map(int, input().split()) # N개중 M번째 문서
    document = [ i for i in range(N)]
    importance = list(map(int , input().split()))
    while len(document) > 0 :
        if max(importance) != importance[0]:
            importance.append(importance.pop(0))
            document.append(document.pop(0))
        else:
            importance.pop(0)
            cnt+=1
            if document[0] == M:
                break
            else:
                document.pop(0)
    result.append(cnt)
    
for i in result:
    print(i)