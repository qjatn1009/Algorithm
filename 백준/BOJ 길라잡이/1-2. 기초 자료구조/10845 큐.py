import sys
N = int(sys.stdin.readline())
que, result = [], []
for i in range(N):
    order = sys.stdin.readline()
    if "push" in order:
        que.append(int(order[5:]))

    elif "pop" in order:
        if len(que) == 0:
            result.append(-1)
        else:
            result.append(que.pop(0))

    elif "size" in order:
        result.append(len(que))

    elif "empty" in order:
        if len(que) == 0:
            result.append(1)
        else:
            result.append(0)

    elif "front" in order:
        if len(que) == 0:
            result.append(-1)
        else:
            result.append(que[0])

    elif "back" in order:
        if len(que) == 0:
            result.append(-1)
        else:
            result.append(que[-1])

for i in result:
    print(i)