bj=int(input())
n=0
for i in range(0,bj):
  if(pow(2,i)>bj):
    break
  n=bj-pow(2,i)
print(n)
