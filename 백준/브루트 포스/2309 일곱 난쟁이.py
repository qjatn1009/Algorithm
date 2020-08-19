people,result,results = [], False,[]
for i in range(9):
    height = int(input())
    people.append(height)
people.sort()
for i in range(9):
    for j in range(9):
        if i==j:
            pass
        elif sum(people)-(people[i]+people[j])==100:
            result=True
            break
    if result:
        break
for k in range(9):
    if k ==i or k==j:
        pass
    else:
        print(people[k])
