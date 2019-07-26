su=int(input())
li=list(map(int,input().split()))
a=0
c=1
for i in range(len(li)):
    b=0
    for j in range(len(li)):
        if a!=b and c==1:
            if li[a]+li[b]==0:
                print(li[a],li[b])
                c+=1
        b+=1
    a+=1
