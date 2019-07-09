str3=input()
s=0
for n in range(len(str3)):
  if(str3[n].isdigit() or str3[n].isalpha() or str3[n]==(" ")):
    continue
  else:
   s+=1
print(s)
