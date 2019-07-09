p,q=map(int,input().split())
z=list(map(int,input().split()[:p]))
for i in range(0,q):
    if z[i]==q:
        print("yes")
        break
else:
    print("no")
