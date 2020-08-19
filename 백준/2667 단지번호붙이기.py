import sys          #  백준 2667번 단지번호 붙이기
n=int(input())
arr=[]
for i in range(n):
    temp=[]
    x=input()
    for j in range(n):
        temp.append(int(x[j]))
    arr.append(temp)

def danji(start_row,start_colume,temp):
    count=1
    temp[start_row][start_colume] =2
    if start_row+1<n and temp[start_row+1][start_colume] ==1: #row+1가 n이하이고 아래값이 1이면
        count +=danji(start_row+1,start_colume,temp) #아래 노드에서 다시 확인
    if start_row-1>=0 and temp[start_row-1][start_colume] ==1: #row-1가 0이상이고 윗값이 1이면
        count +=danji(start_row-1,start_colume,temp)#윗 노드에서 다시 확인
    if start_colume+1<n and temp[start_row][start_colume+1] ==1: #colume+1이 n이하이고 오른쪽값이 1이면
        count += danji(start_row,start_colume+1,temp) #오른 노드에서 다시 확인
    if start_colume-1>=0 and temp[start_row][start_colume-1]==1: #colume-1이 0이상이고 왼쪽값이 1이면
        count+=danji(start_row,start_colume-1,temp) #왼쪽 노드에서 다시 확인
    return count # 연결된 집의 갯수를 반환

cnt=0  #단지 수
result=[] # 단지마다 연결된 집의 수수
for i in range(n):
    for j in range(n):
        if(arr[i][j]==1):
            result.append(danji(i,j,arr))
            cnt+=1
print(cnt)
result.sort()
for i in result:
    print(i)