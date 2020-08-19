T = int(input())
result = []
for i in range(T):
    VPS = []
    bracket = input()
    for j in range(len(bracket)):
        if bracket[j] == "(":
            VPS.append(bracket[j])
        elif bracket[j] == ")" and j == 0 :
            VPS.append(-1)
            break
        elif bracket[j] == ")" and len(VPS) == 0:
            VPS.append(-1)
            break
        else:
            VPS.pop()
    if len(VPS) == 0:
        result.append("YES")
    else:
        result.append("NO")

for i in result:
    print(i)