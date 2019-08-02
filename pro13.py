b1,n1=map(int,input().split())
s=list(map(int,input().split()))
list=[]
lr=[]
for i in range(n1):
    list=input().split()
    lr.append(min(s[int(list[0])-1:int(list[1])]))
for i in lr:
    print(i,end='\n')
