b=int(input())
j=0
for n in range(2,b):
 if(b%n==0):
  j=j+1
if(j<=0):
 print("yes")
else:
 print("no")
