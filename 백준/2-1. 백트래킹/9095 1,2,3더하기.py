T = int(input())
result = []
def plus(index, n, lists):
    global count
    if index == n:
        if sum(lists) == number:
            count += 1
        return

    for i in range(1,4):
        lists[index] = i
        plus(index+1, n, lists)
        lists[index] = 0
        
for i in range(T):
    count = 0
    number = int(input())
    for i in range(1,number+1):
        lists = [0] * i
        plus(0, i, lists)
    result.append(count)

for i in result:
    print(i)
    