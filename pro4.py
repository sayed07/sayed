pp,qq=map(str,input().split())
was=0
if len(pp)>len(qq):
  pp,qq=qq,dbj
i=0
while n<len(vs):
  was+=(ord(qq[n])-ord(pp[n]))
  n+=1
for r in range(r,len(qq)):
  was+=ord(qq[r])-ord('a')+1
print(was)
