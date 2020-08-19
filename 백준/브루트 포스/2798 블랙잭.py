import sys 
from itertools import combinations
N,M=map(int, sys.stdin.readline().split())
card=list(map(int,sys.stdin.readline().split()))
result=[]
for i in list(combinations(card,3)):
    if M>=(i[0]+i[1]+i[2]):
        result.append((i[0]+i[1]+i[2]))
print(max(result))