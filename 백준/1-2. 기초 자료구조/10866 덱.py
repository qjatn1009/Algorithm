N = int(input())
deque, result, cnt = [], [], 0
for i in range(N):
    order = input()
    if "push_front" in order:
        order = order.split()
        deque.insert(0, int(order[1]))
        cnt+=1

    elif "push_back" in order:
        order = order.split()
        deque.append(int(order[1]))
        cnt+=1

    elif "pop_front" in order:
        if cnt == 0:
            result.append(-1)
        else:
            result.append(deque.pop(0))
            cnt-=1
    
    elif "pop_back" in order:
        if cnt == 0:
            result.append(-1)
        else:
            result.append(deque.pop())
            cnt-=1

    elif "size" in order:
        result.append(cnt)

    elif "empty" in order:
        if cnt == 0:
            result.append(1)
        else:
            result.append(0)

    elif "front" in order:
        if cnt == 0:
            result.append(-1)
        else:
            result.append(deque[0])

    elif order == "back":
        if cnt == 0:
            result.append(-1)
        else:
            result.append(deque[-1])
for i in result:
    print(i)

