n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

# 방법 1
num.sort(reverse=True)
print(*num)
# 방법 2
for i in sorted(num, reverse= True):
    print(i, end =" ")    