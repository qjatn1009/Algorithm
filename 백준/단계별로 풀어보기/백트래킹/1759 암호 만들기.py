L, C = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()
collection = []
for i in range(C):
    for j in ['a', 'e', 'i', 'o', 'u']:
        if alphabet[i] == j:
            collection.append(i)
check = [0] * C
arr = [0] * L
def dfs(index, num):

    if index == L:
        p, q = 0, 0 # p : 자음 q : 모음
        for i in range(C):
            if check[i] == 1:
                if i in collection:
                    q += 1
                else:
                    p += 1
        if p >= 2 and q >= 1:
            print(''.join(arr))
        return 
    for i in range(num, C):
        if check[i] == 0:
            check[i] = 1
            arr[index] = alphabet[i]
            dfs(index + 1, i)
            check[i] = 0
        
dfs(0, 0)