N = int(input())
number = list(map(int, input().split()))
print(*sorted(set(number)))