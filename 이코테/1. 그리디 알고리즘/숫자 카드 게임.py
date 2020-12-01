# 행 중에서 최솟값중 가장 큰 값 출력
N, M = map(int, input().split())
result = 0
for i in range(N):
    min_number = min(list(map(int, input().split())))
    if result < min_number:
        result = min_number
print(result)