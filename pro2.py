from itertools import combinations
pp,qq=list(input().split())
n=[]
pp=int(qq)
l=combinations(pp,len(qq)-qq)
for r in l:
  n.append("".join(r))
print(min(n))
