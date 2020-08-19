N = int(input())
location = []
for i in range(N):
    location.append(list(map(int, input().split())))
    
for i in sorted(location, key= lambda x: (x[1], x[0])):
    print(*i)