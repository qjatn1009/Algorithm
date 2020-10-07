# 구현인데 어려웠음.
def solution(s):
    answer = 0
    result, string = [], ""
    if len(s) <= 2:
        answer = len(s)
    else:
        for i in range(1, len(s)//2 + 1):
            count = 1
            test_str = s[:i]
            for j in range(i, len(s), i):
                if s[j:j+i] == test_str:
                    count += 1
                else:
                    if count == 1:
                        count = ""
                    string += str(count)+test_str
                    test_str = s[j:j+i]
                    count = 1
            if count == 1:
                count = ""
            string += str(count) + test_str
            result.append(len(string))
            print(string)
            string = ""

        answer = min(result)
    return answer

ss = ["bcacacacacaca"]
for i in ss:
    print(solution(i))