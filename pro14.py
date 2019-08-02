b=input()
n=map(int,input().split())
f=[]
for i in n:
    enum=bin(i)
    f.append(enum)
fraud=sorted(f)
fraud.reverse()
for r in fraud:
    print(int(r,2))
