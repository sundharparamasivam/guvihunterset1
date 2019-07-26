su=int(input())
a=list(map(int,input().split()))
l=[]
l1=[]
for i in a:
    if i not in l:
        l.append(i)
    elif i in l and i not in l1:
        l1.append(i)
for i in l1:
    print(i,end=" ")
