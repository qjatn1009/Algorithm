def solution(numbers, hand):
    answer = ''
    left_loca, right_loca = [3,1], [3,3]
    for i in numbers:
        location = [0, 0]
        left, right = 0, 0
        if i == 1 or i == 4 or i == 7 :
            answer += "L"
            left_loca[0] = i // 3
            left_loca[1] = i % 3
        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            right_loca[0] = i // 3  - 1
            right_loca[1] = 3
        else:
            if i == 0:
                location[0] = 3
                location[1] = 2
            else:
                location[0] = i // 3
                location[1] = i % 3
            for j in range(2):
                left += abs(location[j] - left_loca[j])
                right += abs(location[j] - right_loca[j])
            if left < right:
                answer += 'L'
                left_loca = location
            elif left > right:
                answer += 'R'
                right_loca = location
            else:
                if hand == 'right':
                    answer += 'R'
                    right_loca = location
                else:
                    answer += 'L'
                    left_loca = location


    return answer



