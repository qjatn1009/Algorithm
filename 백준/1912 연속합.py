# n = int(input())
# a = list(map(int, input().split()))
# sum = [a[0]]
# for i in range(len(a) - 1):
#     sum.append(max(sum[i] + a[i + 1], a[i + 1]))
# print(sum)

import json
summary = input().split("/")
data = summary[0]
target_value = summary[1]
data = json.loads(data)
def get_summary(data, target_value):
    result = []
    for dic in data:
        if dic["value"] == target_value and dic["is_active"]:
            i = dic["parent"]
            result.append(dic["value"])
            while i != None:
                if data[i - 1]["is_active"]:
                    result.insert(0, data[i - 1]["value"])
                    i = data[i - 1]["parent"]
                else:
                    result = ["INACTIVE"]
                    break
    if len(result) == 0:
        return "INACTIVE"
    elif len(result) <= 3:
        return ">".join(result)
    else:
        return ">".join(result[len(result) - 3:])
print(get_summary(data, target_value))