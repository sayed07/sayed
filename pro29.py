inp=int(input())

bb=0

nn=0

a=[]

while bb<90 and bb<inp:

  s=0

  for j in str(inp-bb):

    s+=int(j)

  if s+(inp-bb)==inp:

    nn+=1

    a.append(inp-bb)

  bb+=1

print(nn)

for bb in a:

  print(bb)
