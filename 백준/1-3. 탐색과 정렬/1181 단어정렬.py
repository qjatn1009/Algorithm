N = int(input())
strings = []
for i in range(N):
    strings.append(input())

for i in sorted(set(strings), key = lambda x: (len(x), x)):
    print(i)