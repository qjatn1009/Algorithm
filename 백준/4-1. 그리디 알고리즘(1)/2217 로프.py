N = int(input())
rope, weight = [], 0
for i in range(N):
    rope.append(int(input()))
rope.sort(reverse= True)

for k in range(1, N+1):
    if weight < rope[k-1]*k:
        weight = rope[k-1]*k
print(weight)