bb=input()
nn=list(map(int,input().split()))
maximum=0
r=0
while(r<len(nn)-1):
    count=0
    while(r<len(nn)-1 and nn[r]<nn[r+1]):
        count+=1
        r+=1
    if(count>maximum):
        maximum=count
    r+=1
print(maximum+1)
