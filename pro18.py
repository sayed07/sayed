nn,mm=map(int,input().split())
tem=[]
z=0
for n in range(nn):
    tem.append(list(map(int,input().split())))   
for n in range(nn):
    for i in range(mm-1):
        for r in range(i+1,mm+1):
            if tem[n][i:r]==[1]*len(tem[n][i:r]):
                 if all(tem[q+n][i:r]==[1]*len(tem[q+n][i:r]) for q in range(len(tem[n][i:r])-1)):
                     if len(tem[n][i:r])>z:
                        x=len(tem[n][i:k])
if len(tem)==1 and len(tem[0])==1 and tem[0][0]==1:
    print(1)
for n in range(z):
    print(*[1]*z) 
