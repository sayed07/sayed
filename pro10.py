bb1=int(input())
nn1=list(map(int,input().split()))
jj1=0
for i in range(0,bb1):
    for r in range(0,i):
        if nn1[r]<nn1[i]:
            jj1=jj1+nn1[r]
print(jj1)
