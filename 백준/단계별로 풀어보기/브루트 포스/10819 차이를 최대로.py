n = int(input())
num = list(map(int, input().split()))
check = [0] * n
arr = [0] * n
answer = 0

def get_total(arr):
    total = 0
    for i in range(n - 1):
        if arr[i] - arr[i + 1] > 0 :
            total += arr[i] - arr[i + 1]
        else:
            total += arr[i + 1] - arr[i]
    return (total)

def dfs(index):
    global answer
    if index == n:
        answer = max(answer, get_total(arr))
        return
    for i in range(n):
        ind = i + index
        if ind >= n:
            ind -= n
        if check[ind] == 0:
            check[ind] = 1
            arr[index] = num[ind]
            dfs(index + 1)
            check[ind] = 0
            arr[index] = 0
dfs(0)
print(answer)