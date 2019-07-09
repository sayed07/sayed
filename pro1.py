pp=int(input())
qq=[]
for n in range(0,pp):
 lan=input()
 qq.append(lan)
thissss=[]
for n in zip(*qq):
 if(n.count(n[0])==len(n)):
  thissss.append(n[0])
 else:
  break
print(''.join(thissss))
