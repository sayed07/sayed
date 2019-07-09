n=input()
for i in range(0,len(n)):
    
    if (n[i].isalpha() and n[i].isnumeric()):
        print("No")
else:
        print("Yes")
