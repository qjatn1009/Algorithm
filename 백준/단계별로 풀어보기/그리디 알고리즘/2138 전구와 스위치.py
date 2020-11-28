N = int(input())
test =  list(input())
end = list(input())
def change(value):
    if value == '1':
        value = '0'
    else:
        value = '1'
    return value

def check(num, test):
    start, count = [], 0
    for i in test:
        start.append(i)
    for i in range(num, N):
        if i == 0:
            for j in range(3):
                    if 0 <= (i - 1 + j) < N:
                        start[i - 1 + j] = change(start[i - 1 + j])
            count += 1
        else:
            if start[i - 1] != end[i - 1]:
                for j in range(3):
                    if 0 <= (i - 1 + j) < N:
                        start[i - 1 + j] = change(start[i - 1 + j])
                count+= 1
    if start == end:
        return (count)
    else:
        return (-1)
result = []
for i in range(2):
    count = check(i, test)
    if count != -1:
        result.append(count)        

if len(result) == 0:
    print(-1)
else:
    print(min(result))
