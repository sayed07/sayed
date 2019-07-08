p=int(input())
q=list(map(int,input().split()[:p]))
q.sort()
for r in q:
   print(r,end=" ")
