# 소름 돋게 어려움...
from math import sqrt

min_number, max_number = map(int, input().split())
root, check = [], [False,False] + [True] * (int(sqrt(max_number)) + 1)
result = [True] * (max_number - min_number + 1)
answer = 0
def is_Prime(numbers):
    for i in range(2,numbers+1):
        if check[i]:
            root.append(i**2)
        for j in range(i*2, numbers+1, i):
            check[j] = False

is_Prime(int(sqrt(max_number)))
for i in root:
    if min_number % i == 0:
        number = min_number
    else:
        number = min_number + i - (min_number % i)
    for j in range(number - min_number, len(result), i):
        result[j] = False

for i in result:
    if i:
        answer += 1
print(answer)
