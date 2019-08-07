nn=int(input())
bb=list(map(int,input().split()))
bb.sort()
sin=0
pp=0
for i in range(len(bb)):
    if bb[i]>=sin:
        pp=pp+1
    sin=sin+bb[i]
print(pp)
