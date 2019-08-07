nn=input()
bb=0
for r in range(0,len(nn)):
    s=n1[0:r]+nn[r+1::]
    if int(s)%8==0:
        bb=1
        break
if bb==1:
    print("yes")
else:
    print("no")
