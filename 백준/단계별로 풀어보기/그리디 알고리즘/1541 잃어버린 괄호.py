expression = input()
number, operator = [], []
num = ""
for i in expression:  
    if i == '-' or i == '+':
        number.append(int(num))
        operator.append(i)
        num = ""
    else:
        num += i
number.append(int(num))
result = [number[0]]
for i in range(len(operator)):
    if operator[i] == '-':
        result.append(number[i+1])
    else:
        result[-1] += number[i+1]

min_number = 0
for i in range(len(result)):
    if i == 0:
        min_number = result[i]
    else:
        min_number -= result[i]

print(min_number)