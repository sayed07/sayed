pp,qq=map(int,input().split())
lis=list(map(int,input().split()))
pp=[]
lis.insert(0,0)
for r in range(qq):
     vin=[]
     j=0
     aa,bb=map(int,input().split())
     for i in range(aa,bb+1):         
         j^=lis[i]     
     pp.append(j)
for r in pp:
     print(r)
