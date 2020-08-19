n, m = map(int, input().split())
result = [0 for _ in range(m)]

def sequence(index, n, m):
    if index == m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return

    for i in range(1, n + 1):
        result[index] = i
        sequence(index + 1, n, m)

sequence(0, n, m)