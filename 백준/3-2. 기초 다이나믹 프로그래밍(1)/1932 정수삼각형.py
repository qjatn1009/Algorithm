# top - bottom 방식
n = int(input())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))

def solve(index):
    
    for i in range(1, index):
        for j in range(len(t[i])):                
            if j == 0:
                t[i][j] += t[i-1][0]
            elif j == len(t[i])-1:
                t[i][j] += t[i-1][-1]
            else:
                t[i][j] += max(t[i-1][j-1], t[i-1][j])
    return max(t[i])

print(solve(n))