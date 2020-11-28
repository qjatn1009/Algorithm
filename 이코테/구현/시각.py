n = int(input())
result = 0
# h 3 미포함
# 분에 3 포함 : 16개 * 60개
# 분에 3 미포함 : 44개 * 16개

# h 3 포함
# 60 * 60
for i in range(n + 1):    
    if i == 3 or i == 13:
        result += 3600
    else:
        result += 45 * 15
        result += 15 * 60
print(result)