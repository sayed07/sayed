nn=input()
bb=0
ms=[]
for r in range(0,len(nn)-1):
    for n in range(r+1,len(nn)):
        k=nn[r:n+1]
        l=k[::-1]
        if k==l:
            ms.append(len(nn)-len(l))
print(min(ms))
