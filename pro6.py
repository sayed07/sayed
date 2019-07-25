l=int(input())
list1=[]
lis=list(map(int,input().split()))
for r in range(len(lis)):
    for n in range(r+1,len(lis)):
        for r in range(n+1,len(lis)):
            if (lis[r]< lis[n] and lis[n]<lis[r])and (r<n and j<r):
                a=[lis[r],lis[n],lis[r]]
                if l in list1:
                    continue
                else:
                    list1.append(l)
print(len(list1))
