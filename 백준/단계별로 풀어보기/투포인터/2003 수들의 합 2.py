N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for i in range(N):
    result = A[i]
    if result > M:
        continue
    elif result == M:
        cnt += 1
        continue
    else:
        for j in range(i+1, N):
            result += A[j]
            if result > M:
                break
            elif result == M:
                cnt += 1
                break
print(cnt)