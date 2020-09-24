N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split())) # +, -, *, //
count = sum(operators)
result = [0]*sum(operators)
Maxvalue, Minvalue = -1000000000, 1000000000
# 전부다 배치하는 방법
def Calculation(result):
    order = numbers[0]
    for i in range(len(result)):
        if result[i] == 0:
            order+=numbers[i+1]
        elif result[i]== 1:
            order-=numbers[i+1]
        elif result[i]== 2:
            order*=numbers[i+1]
        else:
            if order < 0:
                order = -(abs(order)//numbers[i+1])
            else:
                order//=numbers[i+1]
    return order

def arrangement(index):
    global Maxvalue, Minvalue
    if index == count:
        Maxvalue = max(Maxvalue, Calculation(result))
        Minvalue = min(Minvalue, Calculation(result))
        return

    for i in range(len(operators)):
        if operators[i]== 0:
            continue
        result[index]=i
        operators[i]-=1
        arrangement(index+1)
        operators[i]+=1
arrangement(0)
print(Maxvalue)
print(Minvalue)