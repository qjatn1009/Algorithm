from math import sqrt
# numbers, count = [],

def isPrime(a): #소수 판별법
  if(a<2):
    return False
  for i in range(2,int(sqrt(a)+1)):
    if(a%i==0):
      return False
  return True

T = int(input())

for i in range(T):
    possible = True
    length = sum(list(map(int, input().split())))
    if length >= 4 and length % 2 == 0:
        print("YES")
        continue
    else:
        if isPrime(length-2):
            print("YES")
            continue
        else:
            print("NO")        
    
    # for i in range(2,(length//2)+1):
    #     if i > 2 and i % 2 == 0:
    #         continue
    #     if isPrime(i) and isPrime(length-i):
    #         print("YES")
    #         possible = False
    #         break
    # if possible:
    #     print("NO")

