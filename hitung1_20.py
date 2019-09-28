from datetime import datetime
frmt = '%H:%M:%S'
start = datetime.now().strftime(frmt)

print(start)
a = 1
b = False
while True:
  for i in range(1,21):
    if a % i != 0:
      b = False
      break
    else:
      b = True
  if b :
    print(a)
    end = datetime.now().strftime(frmt)
    dtime = datetime.strptime(end,frmt)-datetime.strptime(start,frmt)
    print(dtime)
    break
  a += 1  
