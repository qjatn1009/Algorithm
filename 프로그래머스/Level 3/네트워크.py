from collections import deque

def solution(n, computers):
    answer = 0
    check = [0] * n
    group = 1
    for i in range(n):
        move = deque()
        move.append(i)
        if check[i] == 0:
            while move:
                number = move.popleft()
                check[number] = group
                for j in range(n):
                    if number == j:
                        continue
                    elif computers[number][j] == 1:
                        computers[number][j] = 0
                        move.append(j)
            group += 1
    answer = group - 1

    return answer




print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))