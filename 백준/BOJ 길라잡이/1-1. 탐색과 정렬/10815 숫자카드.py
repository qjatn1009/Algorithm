import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()
result = []

def binary_search(i):
    low, high = 0, N-1
    while low <= high:
        mid = (low+high) //2
        if N_list[mid] > i:
            high = mid -1
        elif N_list[mid] < i:
            low = mid + 1
        else:
            return 1
    return 0

for i in M_list:
    result.append(binary_search(i))

print(*result)