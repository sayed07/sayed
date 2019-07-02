p,q=map(int,input().split())
for i in range(p+1,q):
  ch=i
  x=0
  while (i>0):
    b=i%10
    x=x+(b**3)
    i=i//10
    if(x==ch):
      print(fnd,end=" ")
