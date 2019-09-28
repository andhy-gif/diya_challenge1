stop = True
a = 0
while stop:
  for b in range(a+1):
    c = int(((a*a)+(b*b))**(1/2))
    if (a*a) + (b*b) == (c*c) and a + b + c == 1000:
      print('a = {}, b = {}, c = {}'.format(a,b,c))
      stop = False
  a += 1
