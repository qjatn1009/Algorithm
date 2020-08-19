N, M = map(int, input().split())
prices= []
Minprice, benfit = 0, 0
for i in range(M):
    prices.append(int(input()))
prices.sort()
for i in range(M):
    customer = 0
    for j in range(i,M):
        if customer == N:
            break
        elif prices[i]<=prices[j]:
            customer+=1
    if prices[i]*customer > benfit:
        benfit = prices[i]*customer
        Minprice = prices[i]

print(Minprice, benfit)