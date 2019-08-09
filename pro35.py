import sys,string
def freq1(a) :
    din = {}
    for b in a :
        din[b] = din.get(b,0) + 1
    return din
 
a = input()
n = len(a)
din = freq1(a)
Lk = list(din.keys())
#print(din,Lk)
 
for j in range(n-2,-1,-1) :
    #print('len = ', j+1)
    for b in Lk :
        kin = 0
        for i in range(0,n-j) :
            li, ri = i,j+i
            a2 = a[li:ri + 1]
            #print(b,a2)
            if b in a2 :
                kin += 1
        if kin == n-j :
            #print('b,kin',b,kin)
            b2 = b
            kin2 = kin
            len2 = j+1
print(len2)
