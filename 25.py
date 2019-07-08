#import math      
s=int(input())
n=list(map(int,input().split()))[:s]
a=n.sort()
middleIndex =int( (len(n))/2)
#print(math.ceil(middleIndex))
print(n[middleIndex])
