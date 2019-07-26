su=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if(all(x in a for x in b)):
    print("YES")
else:
    print("NO")
