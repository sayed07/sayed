nn = int(input())
lis = list(map(int, input().split()))
maximum = 0
cont = 0
for r in range(nn-1):
    if lis[r] < lis[r+1]:
        cont +=1
        if maximum < cont:
            maximum = cont
    else:
        cont = 0
print(maximum+1)
