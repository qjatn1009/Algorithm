N = int(input())
colonnade, colonnade_distance = [], []
max_distance = 0
for i in range(N):
    colonnade.append(int(input())) 
colonnade.sort()
for i in range(N-1):
    colonnade_distance.append(colonnade[i+1]-colonnade[i])

for i in range(min(colonnade_distance),0, -1):
    check= True
    for j in colonnade_distance:
        if j % i != 0:
            check = False
            break
    if check:
        max_distance = i
        break
result = (colonnade[-1]-colonnade[0]) / max_distance - N + 1
print(int(result))
