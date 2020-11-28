# N이 1이 될 때까지 반복
# 1. N - 1한다. 2. N // K
# 2 <= K <= N <= 100000
N, K = map(int, input().split())
result = 0
while (True):
    if N == 1 or N == 0:
        break
    if N % K == 0:
        N //= K
        result += 1
    else:
        result += N % K
        N -= N % K
if N == 1:
    print(result)
else:
    print(result - 1)