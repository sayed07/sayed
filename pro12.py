p1,q1=map(int,input().split())
lis=list(map(int,input().split()))
z=[]
for i in range(0,q1):
     b21,n21=map(int,input().split())
     z.append([b21,n21])
for i in range(q1):
     lower=z[i][0]
     upper=z[i][1]
     s=sum(lis[lower-1:upper])
     print(s)
