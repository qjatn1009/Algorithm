N = int(input())
P = list(map(int, input().split()))
P.sort()
result = 0
for i in range(N):
    result += N * P[i]
    N -= 1
print(result)