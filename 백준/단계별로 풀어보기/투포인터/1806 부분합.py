N, M = map(int, input().split())
A = list(map(int, input().split()))
start, end = 0, 0
result, cnt = 0, []
while start < N:
    if end == N:
        if result < M:
            break
        else:
            result -= A[start] # start를 한칸 뒤로
            cnt.append(end-start)
            start += 1
    else:
        if result < M : # 값이 낮을 경우
            result += A[end] # end를 한 칸 뒤로
            end += 1
            
        else : # 값이 크거나 같을 경우
            result -= A[start] # start를 한칸 뒤로
            cnt.append(end-start)
            start += 1


if len(cnt) == 0:
    print(0)
else:
    print(min(cnt))