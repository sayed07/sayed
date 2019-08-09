pp,qq=map(int,input().split())
bb=0
Lis=[]
for i in range(pp):
      Lis.append(input())
for i in range(pp):
      for j in range(qq-1):
            if(Lis[i][j]!='R' and Lis[i][j+1]!='R'):
                  bb+=3
            elif(Lis[i][j]!='G' and Lis[i][j+1]!='G'):
                  bb+=5
print(bb)
