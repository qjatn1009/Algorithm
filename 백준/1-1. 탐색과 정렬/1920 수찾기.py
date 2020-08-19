import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
result = []

for i in M_list:
    if i in N_list:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)