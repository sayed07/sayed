def subb(n): 
    bil= len(n) 
    subb = [1]*bil
    for r in range (1 , bil): 
        for j in range(0 , r): 
            if n[r] > n[j] and subb[r]< subb[j] + 1 : 
                subb[r] = subb[j]+1
    maximum = 0
    for r in range(bil): 
        maximum = max(maximum , subb[r])  
    return maximum
ar1=int(input()) 
n = list(map(int,input().split()))
print (subb(n))
