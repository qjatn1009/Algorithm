import sys   #백준 1339번 단어 수학
N=int(sys.stdin.readline())
arr=[0 for i in range(26)]
temp=[9,8,7,6,5,4,3,2,1]
for i in range(N):
    line=sys.stdin.readline()
    k=len(line)-2
    for j in line[:len(line)-1]:
        arr[ord(j)-ord('A')]+=pow(10,k)  #ord는 알파벳을 아스키코드 pow는 제곱승 사용
        k-=1
arr.sort(reverse=True)
result=0
for i in range(9):
    result+=arr[i]*temp[i]
print(result)