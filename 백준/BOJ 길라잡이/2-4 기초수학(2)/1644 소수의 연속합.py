N = int(input())
numbers, count = [], 0
a = [False,False] + [True]*(N-1)

for i in range(2,N+1):
    if a[i]:
        numbers.append(i)
    for j in range(2*i, N+1, i):
        a[j] = False
        
for i in range(len(numbers)):
    sum = 0
    for j in range(i,len(numbers)):
        if sum+numbers[j] > N:
            break
        elif sum+numbers[j] == N:
            count += 1
            break
        else:
            sum += numbers[j]
print(count)
