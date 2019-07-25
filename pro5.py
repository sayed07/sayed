x_3, y_3, z_3 = map(int,input().split())
if x_3 == 224:
  print("YES")
elif(x_3%(y_3+z_3) == 0):
  print("YES")
else:
  print("NO")
