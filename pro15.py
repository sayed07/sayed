pp=input()
qq=map(int,input().split())
aa=[]
for r in qq:
    enum=bin(r)
    aa.append(enum)
fraud=sorted(aa)
fraud.reverse()
for n in fraud:
    print(int(n,2))
