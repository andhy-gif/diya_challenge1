def kelipatan_3_dan_5(x):
  if x % 3 == 0 and x % 5 == 0:
    return True
  else:
    return False

for i in range(1,101):
  if kelipatan_3_dan_5(i):
    print(i)
  

