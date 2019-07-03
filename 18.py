p,q=map(int,input().split())
for i in range(p+1,q):
  ch=i
  fnd=0
  while (i>0):
    r=i%10
    fnd=fnd+(r**3)
    i=i//10
    if(fnd==ch):
      print(fnd,end=" ")
