p,q=map(int,input().split())
n=list(map(int,input().split()[:p]))
count=0
for i in range(0,p):
    if(n[i]==q):
        count=count+1
print(count)
