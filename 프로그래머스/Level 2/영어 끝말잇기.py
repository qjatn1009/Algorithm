def solution(n, words):
    answer = []
    previous = words[0][0]
    pre_words, num, cnt = [], 1, 1
    for i in words:

        if previous == i[0]: # 맨뒤 알파벳과 다음 단어 첫 알파벳 일치
            if i in pre_words: #이미 말했던 단어
                answer.append(num)
                answer.append(cnt)
                break
            else: # 처음 말하는 단어
                pre_words.append(i)
        else: # 끝말잇기를 실패
            answer.append(num)
            answer.append(cnt)
            break
        previous = i[-1]
        num += 1
        if num > n:
            num %= n
            cnt += 1
    if len(answer) == 0:
        answer = [0, 0]
        

    return answer

print(solution(3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))