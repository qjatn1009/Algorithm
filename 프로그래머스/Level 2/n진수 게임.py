#테케는 맞는데 답은 아님
def solution(n, t, m, p):
    answer = ''
    result, i, num= '0', 0, 0
    while len(result) < t*2:
        notation = ''
        i = num
        while i > 0 :
            if i % n >= 10:
                notation += chr((i % n )+ 55)
            else:
                notation += str(i % n)
            i //= n
        if notation[::-1] != None:
            result += notation[::-1]
        num += 1

    for i in range(2*t):
        if i % m == p-1:
            answer += result[i]
        
    return answer
    
print(solution(2, 4, 1, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))