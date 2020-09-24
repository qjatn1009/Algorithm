N = int(input())
meeting, count = [], 1
for i in range(N):
    meeting.append(list(map(int, input().split())))

meeting.sort()
start, end = meeting[0][0], meeting[0][1]
for i in range(1, len(meeting)):
    if meeting[i][1] < end:
        start = meeting[i][0]
        end = meeting[i][1]
    else:
        if meeting[i][0] < end < meeting[i][1]:
            continue
        elif  meeting[i][0] >= end:
            start = meeting[i][0]
            end = meeting[i][1]
            count += 1
print(count)