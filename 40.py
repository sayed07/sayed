num=int(input())
p=1
q=1
count=0
while(count<num):
  print(p, end=' ')
  r=p+q
  p=q
  q=r
  count+=1

