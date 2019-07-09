from itertools import combinations
pp,qq=list(input().split())
n=[]
qq=int(qq)
l=combinations(pp,len(pp)-qq)
for r in l:
  n.append("".join(r))
print(min(n))
