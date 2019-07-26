su=int(input())
li=list(map(int,input().split()))
l1=li[::-1]
if sum(li)==0:
  print(0)
else:
  for i in l1:
    print(i,end="")
