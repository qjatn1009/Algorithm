import sys
N = int(sys.stdin.readline())
N_list = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
result = [0] * M
def binary_search(index, i, low):
    high = N-1
    while low < high:
        mid = (low+high) //2
        if N_list[mid] >= i:
            high = mid
        else:
            low = mid + 1
    if i == N_list[low]:
        result[index]+=1
        if low < N-1:
            binary_search(index, i, low+1)
        
for i in range(M):
    binary_search(i, M_list[i], 0)

print(*result)