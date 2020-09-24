k = int(input())
sign = list(input().split())
max_value, max_num, max_count  = [0]*(k+1), 9, 0 
min_value, min_num, min_count  = [0]*(k+1), 0, 0 

for i in range(k+1): #최댓값
    if i == k:
        max_value[i] = max_num
    elif sign[i] == "<":
        max_count += 1
    else:
        for j in range(max_count+1):
            max_value[i-j] = max_num
            max_num -= 1
        max_count = 0
for j in range(max_count+1):
        max_value[i-j] = max_num
        max_num -= 1

for i in range(k+1): #최솟값
    if i == k:
        min_value[i] = min_num
    elif sign[i] == ">":
        min_count += 1
    else:
        for j in range(min_count+1):
            min_value[i-j] = min_num
            min_num += 1
        min_count = 0
for j in range(min_count+1):
    min_value[i-j] = min_num
    min_num += 1
min_count = 0

max_number, min_number = "", ""
for i in range(k+1):
    max_number += str(max_value[i])
    min_number += str(min_value[i])
print(max_number)
print(min_number)