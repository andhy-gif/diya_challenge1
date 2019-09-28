def prima(batas):
  batas
  for a in range(2,batas):
    prima = True 
    for b in range(2,a ):
      if (a % b == 0):
        prima = False
    if (prima):
      
print(prima(10))      

