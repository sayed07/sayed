pp,qq=input().split()
ss=abs(len(pp)-len(qq))
for r in range(len(pp)):
  if len(qq)==1 and qq[r] in pp:
   break
  if pp[r]!=qq[r]:
   ss+=1
print(ss)
