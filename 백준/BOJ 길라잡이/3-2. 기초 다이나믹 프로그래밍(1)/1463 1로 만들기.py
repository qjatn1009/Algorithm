N = int(input())
result = [0, 0]

def make_one(number):
    for i in range(2, number+1):
        if i % 6 == 0:  # 3과 2로 나눠 지는 경우
            result.append(min(result[i//3], result[i//2], result[i-1])+1)
        elif i % 3 == 0: # 3으로 나눠 지는 경우
            result.append(min(result[i//3], result[i-1])+1)
        elif i % 2 == 0: # 2로 나눠 지는 경우 
            result.append(min(result[i//2], result[i-1])+1)
        else:  # 3과 2로 안나눠 지는 경우
            result.append(result[i-1]+1)

make_one(N)
print(result[N])
