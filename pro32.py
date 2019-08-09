bb,nn=map(int,input().split())
pp=[]
for i in range(0,bb):
    mn=[int(n) for n in input().split()]
    pp.append(sorted(mn))
for i in range(0,len(pp[0])):
  #print(pp[i])
  for j in range(0,len(pp)-1):
    if pp[j][i]>pp[j+1][i]:
      pp[j][i],pp[j+1][i]=pp[j+1][i],pp[j][i]
for i in pp:
  print(*i)
