n = int(input())
numbers = [i for i in range(1,n+1)]
stack, result = [], []
inspection = False
k = 0
for i in range(n):
    stack_number = int(input())
    for j in range(k,stack_number):
        stack.append(j)
        result.append('+')
    if k < stack_number:
        k = stack_number
    if stack[-1] != stack_number-1:
        inspection = True
    else:
        stack.pop()
        result.append('-')

if inspection:
    result=['NO']

for i in result:
    print(i)
