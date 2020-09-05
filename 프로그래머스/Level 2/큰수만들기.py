#프로그래머스 큰수 만들기
def solution(number, k):
    answer = ''
    numbers = list(map(int, ''.join(number)))
    stack = [numbers[0]]
    for num in numbers[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k-=1
            stack.pop()
        stack.append(num)
    
    if k > 0:
        for i in stack[k:]:
            answer+=str(i)
    else:
        for i in stack:
            answer+=str(i)
    return answer 
    
print(solution("4177252841", 4))
a = [1,2,3,4,5]
print(a[0:2])