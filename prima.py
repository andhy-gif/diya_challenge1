x = 0
for a in range(2,10):
  prima = True 
  for b in range(2,round(int(a)**0.5) ):
    if (a % b == 0):
      prima = False
  if (prima):
    print (a)
  x += a


print(x)    

