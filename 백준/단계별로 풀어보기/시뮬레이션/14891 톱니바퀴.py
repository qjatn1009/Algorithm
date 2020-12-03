from collections import deque
gears, plan = [], []
for i in range(4):
    gear = deque()
    for j in list(map(int, input())):
        gear.append(j)
    gears.append(gear)
k = int(input())
for i in range(k):
    plan.append(list(map(int, input().split())))

def clockwise(gear_type, gear):
    move = deque(gear)
    if gear_type == 1: #시계
        move.appendleft(move.pop())
    elif gear_type == -1: # 반시계
        move.append(move.popleft())
    return (move)

def get_result(gears):
    score = 0
    for i in range(len(gears)):
        if gears[i][0] == 0:
            continue
        else:
            score += 2**i
    return (score)

def get_state(gears, num, turn):
    possible[num] = False
    if num in [0, 1, 2]:
        if gears[num][2] != gears[num + 1][6] and possible[num + 1]:
            turn_type[num + 1] = -1 * turn
            get_state(gears, num + 1, turn_type[num + 1])
        else:
            possible[num + 1] = False
    if num in [1, 2, 3]:
        if gears[num][6] != gears[num - 1][2] and possible[num - 1]:
            turn_type[num - 1] = -1 * turn
            get_state(gears, num - 1, turn_type[num - 1])
        else:
            possible[num - 1] = False

for i in range(k):
    num, turn = plan[i]
    turn_type = [0, 0, 0, 0]
    possible = [True] * 4
    turn_type[num - 1] = turn
    get_state(gears, num - 1, turn_type[num - 1])
    for j in range(len(turn_type)):
        gears[j] = clockwise(turn_type[j], gears[j])

print(get_result(gears))