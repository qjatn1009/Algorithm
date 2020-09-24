from math import sqrt

def isPrime(a):
  if(a<2):
    return False
  for i in range(2,int(sqrt(a)+1)):
    if(a%i==0):
      return False
  return True

while True:
    N = int(input())
    if N == 0 :
        break
    else:
        possible = True
        for i in range(3,(N//2)+1):
            if i % 2 == 0:
                continue
            if isPrime(i) and isPrime(N-i):
                print("{0} = {1} + {2}".format(N, i, N-i))
                possible = False
                break
        if possible:
            print("Goldbach's conjecture is wrong.")