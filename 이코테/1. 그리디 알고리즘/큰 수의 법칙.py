# N 배열의 크기, M 숫자 더하는 횟수, K 연속해서 더할 수 있는 횟수
# 가장 크게 더하는 값 구하기
# 1번 방안
N, M, K = map(int, input().split())
number = list(map(int, input().split()))
number.sort(reverse=True)
result, count = 0, 0
for i in range(M):
    if count < K:
        result += number[0]
        count += 1
    else:
        result += number[1]
        count = 0
print(result)
# 더 빠른 방안
result += (M // (K+1)) * (K * number[0] + number[1])
result += (M % (K + 1)) * number[0]
print(result)