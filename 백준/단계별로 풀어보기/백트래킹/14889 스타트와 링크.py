from itertools import combinations

N = int(input())
team = [i for i in range(N)]
ability = []
for i in range(N):
    ability.append(list(map(int, input().split())))

start = list(combinations(team, N//2))
link = []

for i in start:
    link_team = [i for i in range(N)]
    for j in i:
        link_team.remove(j)
    link.append(link_team)

def Score(start,link):
    score = 0
    for i in range(len(start)):
        for j in range(len(start)):
            score+=ability[start[i]][start[j]]-ability[link[i]][link[j]]
    return abs(score)


result = []
for i,j in zip(start, link):
    result.append(Score(i,j))

print(min(result))