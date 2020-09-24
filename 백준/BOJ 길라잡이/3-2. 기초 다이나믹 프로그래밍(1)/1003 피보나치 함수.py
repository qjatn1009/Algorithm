# 메모이제이션 사용

T = int(input())
result = [[1,0],[0,1]]
def fibonacci(n):
    if n >= 2:
        for i in range(2, n+1):
            answer = [0,0]
            answer[0] = result[i-1][0] + result[i-2][0]
            answer[1] = result[i-1][1] + result[i-2][1]
            result.append(answer)

fibonacci(40)
for i in range(T):
    number = int(input())
    print(*result[number])