K = int(input())
money = []
for i in range(K):
    order = int(input())
    if order == 0:
        money.pop()
    else:
        money.append(order)
print(sum(money))