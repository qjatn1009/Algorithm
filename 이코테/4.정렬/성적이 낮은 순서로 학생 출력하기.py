n = int(input())
grade = []
for i in range(n):
    name, score = input().split()
    grade.append([name, int(score)])

grade.sort(key = lambda x : x[1])
for i in range(n):
    print(grade[i][0], end = " ")