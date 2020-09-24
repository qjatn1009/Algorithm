N, K = map(int, input().split())
coin, value = [], 0
for i in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)

for i in coin:
    if K >= i:
        value += K // i
        K -= (K // i) * i
print(value)