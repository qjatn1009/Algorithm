#인터넷 참고하였음.
N = int(input())
Sequence = []
possible = True
def check(lists): #수열 확인
    for i in range(1,(len(lists)//2)+1):
        if lists[-i:] == lists[-2*i:-i]:
                return False 
    return True

def stack(index): #수열 하나씩 쌓기
    global possible
    if not possible: #첫번째 값만 뽑기 위함
        return 

    if index == N:
        if possible:
            for i in Sequence:
                print(i, end= '')
            possible = False
        return

    for i in range(1,4):
        Sequence.append(i)
        if check(Sequence): #좋은 수열이면
            stack(index+1)
        Sequence.pop()
            

stack(0)