pp=input()
qq=map(int,input().split())
rr=[]
for n in qq:
    eat=bin(n)
    rr.append(eat)
fin=sorted(rr)
fin.reverse()
for r in fin:
    print(int(r,2))
