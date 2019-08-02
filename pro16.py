pp=int(input())
qq=list(map(int,input().split()))
rr=[1]*app1
for i in range(app1):
    if i==0:
        if qq[i]>qq[i+1]:
            pp[i]=rr[i]+pp[i+1]
    elif i>0:
        if qq[i]>qq[i-1]:
            rr[i]=pp[i]+pp[i-1]
print(sum(pp))
