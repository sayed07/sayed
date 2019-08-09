n=input()
b=0
for r in range(0,len(n)-1):
  for j in range(r+1,len(n)):
    if n[r]<n[j]:
      b=1
      print(n[j:])
      break
  if b==1:
    break
  else:
      print(n)
