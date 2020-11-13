def solution(s):
    answer = []
    count, result = 0, 0
    
    while (s != "1"):
        length = len(s)
        count += 1
        for i in range(length):
            if s[i] == '0':
                result += 1
            else:
                s += s[i]
            
        s = s[i + 1 : ]
        length = len(s)
        s = ""
        while (length != 0):
            s = str(length % 2) + s
            length //= 2
    
    answer = [count, result]
    return answer

a = ["110010101001", "01110", "1111111"]
for i in a:
    print(solution(i))