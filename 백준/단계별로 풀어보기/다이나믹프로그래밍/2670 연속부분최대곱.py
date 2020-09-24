n = int(input())
arr = []

for _ in range(n):
    data = float("{0:0.3f}".format(float(input())))
    arr.append(data)

dp = [arr[0]]

for i in range(1, n):
    dp.append(max(arr[i], dp[i-1]*arr[i]))

print('{0:.3f}'.format(max(dp)))