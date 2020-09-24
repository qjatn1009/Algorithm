import sys

distance, price = [], []
N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
cost, present = distance[0] * price[0], price[0]

for i in range(1, N-1):
    if price[i] > present:
        cost += distance[i] * present
    else:
        cost += distance[i] * price[i]
        present = price[i]
print(cost)