# 시간초과
string = list(input())
M = int(input())
head, tail = string, []
for i in range(M):
    print(head, tail)
    order = input()
    if order[0] == "L": #커서 앞으로 이동
        if len(head) != 0:
            tail.append(head.pop())


    elif order[0] == "D": # 커서 뒤로 이동
        if len(tail) != 0:
            head.append(tail.pop())


    elif order[0] == "B": #커서 왼쪽 문자 삭제
        if len(head)!= 0:
            head.pop()

    elif order[0] == "P": #커서 오른쪽에 글자 추가
        order = order.split()
        head.append(order[1])
        
print(''.join(head)+''.join(tail[::-1]))
