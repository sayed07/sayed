count=int(input())
pp=list(map(int,input().split()))
pp.sort(reverse=True)
#print(pp)
sum=0
sum1=0
qq=[]
for r in range(0,count,2):
    sum=sum+pp[r]
for n in range(1,count,2):
    sum1=sum1+pp[n]
qq.append([sum,sum1])
#print(qq)
for r in qq:
    print(r[0] if r[0]>r[1] else r[1])
