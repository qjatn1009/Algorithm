N = int(input())
stack = []
result = []
for i in range(N):
    order = input()
    if "push" in order:
        stack.append(int(order[5:]))
    elif "pop" in order:
        if len(stack)==0:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif "size" in order:
        result.append(len(stack))
    elif "empty" in order:
        if len(stack)==0:
            result.append(1)
        else:
            result.append(0)
    elif "top" in order:
        if len(stack) ==0:
            result.append(-1)
        else:
            result.append(stack[-1])
for i in result:
    print(i)