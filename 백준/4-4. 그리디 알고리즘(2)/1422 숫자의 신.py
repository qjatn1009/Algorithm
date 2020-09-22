K, N = map(int, input().split())
cnt, result = N - K, []
num, big = [], "0"
for i in range(K):
    num.append(input())
    if int(big) < int(num[-1]):
        big = num[-1]
def compare(a, b):  # 숫자를 하나씩 비교해서 붙여서 높은 걸 선택
    if int(a+b) > int(b+a):
        return True
    else:
        return False

for i in range(K):
    for j in range(i+1, K):
        if compare(num[i], num[j]):
            pass
        else:
            num[i], num[j] = num[j], num[i]

for i in range(K):
    result.append(num[i])    
    if num[i] == big:
        for j in range(cnt): # 가장 높은 수를 cnt만큼 붙힘
            result.append(num[i])
            cnt -= 1
print(''.join(result))