num= int(input())
if num > 1:
   for n in range(2,num):
       if (num % n) == 0:
           print("no")
           break
   else:
       print("yes")
else:
   print("no")
