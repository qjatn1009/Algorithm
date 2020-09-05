count = 0
def target_number(index, numbers, result, target):
    lists = []
    global count
    for i in result:
        lists.append(i+numbers[index])
        lists.append(i-numbers[index])
    if index + 1 != len(numbers):
        target_number(index+1, numbers, lists, target)
    else:
        for i in lists:
            if target == i:
                count += 1

def solution(numbers, target):
    global count 
    answer = 0
    target_number(0, numbers, [0], target)
    answer += count
    
    return answer

print(solution([1,1,1,1,1], 3))