from collections import deque

T = int(input())
result = []
for i in range(T):
    n = int(input())
    student = list(map(int, input().split()))
    possible = [False] * n
    count = n
    for j in range(n):
        if possible[j]:
            continue
        check = [0] * n
        check[j] = 1
        move = deque()
        move.append(student[j])
        while move:
            num = move.popleft() - 1
            if num == j:
                for k in range(n):
                    if check[k] == 1:
                        count -= 1
                        possible[k] = True
                break
            if check[num] == 0 and not possible[num]:
                check[num] += 1
                move.append(student[num])
        possible[j] = True
    result.append(count)

for i in result:
    print(i)