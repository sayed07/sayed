count1=int(input())
pp=[]
qq=[]
for r in range(count1):
    pp.append(list(map(int,input().split())))
for lis in pp:
    for num in lis:
        qq.append(num)
qq.sort()
for r in qq:
    print(r,end=' ')
