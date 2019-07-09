p,q=map(str,input().split())
n=0
if len(p)>len(q):
  p,q=q,p
i=0
while i<len(p):
  n+=(ord(q[i])-ord(p[i]))
  i+=1
for i in range(i,len(q)):
  n+=ord(q[i])-ord('a')+1
print(n)
