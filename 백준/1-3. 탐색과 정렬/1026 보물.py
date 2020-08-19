N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum = 0
for a,b in zip(sorted(A),sorted(B,reverse=True)):
    sum += a*b
print(sum)