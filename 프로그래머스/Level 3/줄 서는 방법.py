def solution(n, k):
    answer = []
    number = 1
    for i in range(1,n+1):
        number *= i
    people = [ i for i in range(1, n+1)]
    k -= 1
    while n > 0:
        number //= n
        answer.append(people.pop(k//number))
        n -= 1
        k -= (k//number)*number
        
    return answer

print(solution(3, 5))