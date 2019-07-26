import math
pp1,qq1=map(int,input().split())
n=[]
j=list(map(int,input().split()))
for r in range(0,q1):
        x,y=map(int,input().split())
        n.append([x,y])
for r in n:
        a1=r[0]-1
        b1=r[1]-1
        print(math.gcd(j[a1],j[b1]))
