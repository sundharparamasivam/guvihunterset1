su=int(input())
li=list(map(int,input().split()))
for i in li:
    a=li.count(i)
    if a>1:
        print(i)
        break
