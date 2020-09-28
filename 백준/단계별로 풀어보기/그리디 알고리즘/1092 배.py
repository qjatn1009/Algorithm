N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))
crane.sort(reverse = True)
box.sort(reverse = True)
time, cnt = 0, 0
check_crane = [True] * N
check_box = [True] * M
if crane[0] < box[0]:
    time = -1
else:
    while True:
        time += 1
        for i in range(N):
            if check_crane[i]:
                for j in range(M):
                    if crane[i] >= box[j] and check_box[j]:
                        check_box[j] = False
                        cnt += 1
                        break
                    if j == M-1:
                        check_crane[i] = False
        if cnt == M:
            break
print(time)