#못품ㄴ

T = int(input())
result = []
for i in range(T):
    reverse = False
    p = list(''.join(input()))
    n = int(input())
    arr=input()
    elements = []
    if n != 0:
        arr = list(map(int,arr[1:-1].split(',')))
    else:
        arr = []
    for order in p:
        if order == 'R':
            if reverse:
                reverse = False
            else:
                reverse = True

        elif order == 'D':
            if len(arr) == 0:
                arr = 'error'
                break
            else :
                if reverse :
                    arr.pop()
                else:
                    arr = arr[1:]
    if arr[-1] == 'error':
        result.append('error')
    else:
        if reverse:
            result.append(arr[::-1])
        else:
            result.append(arr)
print(result)
for i in result:
    if i == 'error':
        print(i)
    else:
        pass