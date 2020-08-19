N, S = map(int, input().split())
number = list(map(int, input().split()))
check = [False] * N
count = 0
# N개의 정수로 이루어진 수열중 1개이상 골라서 원소합이 S인 경우의 수
def Partial_sequence(index, n, result, current): #current는 현재 내가 넣은 원소의 위치
    global count

    if index == n :
        if sum(result) == S:
            count +=1

        return

    else:
        for i in range(current, N):
            if check[i] :
                continue
            result[index] = number[i]
            check[i] = True
            Partial_sequence(index+1, n, result, i)
            check[i] = False
            

for i in range(1,N+1):
    result = [0] * i
    Partial_sequence(0, i, result, 0)

print(count)