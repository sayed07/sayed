b=int(input())
n=list(map(int,input().split()))
s=[1]*b
for r in range(b):
    if r==0:
        if n[r]>n[r+1]:
            s[r]=s[r]+s[r+1]
    elif r>0:
        if n[r]>n[r-1]:
            s[r]=s[r]+s[r-1]
print(sum(s))
