pp=input()
qq=input()
for r in range(len(pp)):
    n1=ord(pp[r])
    r1=ord(qq[r])
    l1=((n1-96)+(r1-96))
    if(l1 > 26)and(l1%26!=0):
        l1=(((n1-96)+(r1-96))%26)+96
        print(chr(l1),end='')
    elif(l1%26==0):
        l1=122
        print(chr(l1),end='')
    else:
        l1=(((n1-96)+(r1-96))+96)
        print(chr(l1),end='')
