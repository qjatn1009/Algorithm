# 줫나 어려움
# N, K = map(int, input().split())
# people = [i for i in range(1, N+1)]
# arr = []
# stack = []
# while len(stack) < N:
#     people = people[K-1:] + people[:K-1]
#     stack.append(people.pop(0))
   
# print("<"+", ".join(str(x) for x in stack)+">")

# N, K = map(int, input().split())
# people = [i for i in range(1, N+1)]
# arr = []
# stack1 = []
# while len(stack1) < N:
#     for remove in range(K-1):
#         people.append(people.pop(0))
#     stack1.append(people.pop(0))

# print(stack)
# print(stack1)


# if stack1 == stack:
#     print("성공")
# print("<"+", ".join(str(x) for x in stack1)+">")

#이해 완료
n,k=map(int,input().split())
js=[ x for x in range(1,n+1)]
out=[]
i=k-1
# print(js)
for x in range(n):
    print('js : ' , js)
    out.append(js.pop(i))
    print('i :', i, 'k-1 :', k-1,'len(js) :', len(js))
    if not js:
        break
    i=(i+k-1)%len(js)
    # k-1씩 더하다가 배열크기 넘어가면 len으로 나누어서 남은 갯수 확인
print("<",end='')
for x in range(len(out)):
    if x==len(out)-1:
        print(out[x],end='')
    else:
        print(out[x],end=', ')
print(">")