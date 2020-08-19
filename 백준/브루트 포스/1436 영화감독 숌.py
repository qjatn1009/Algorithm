import sys
N = int(sys.stdin.readline())
start = 666
count=1
while N>count:
    start+=1
    if "666" in str(start):
        count+=1
print(start)