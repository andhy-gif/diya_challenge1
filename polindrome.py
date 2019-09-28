c = []
for i in range(100,1000):
  for j in range(100,i):
    a = str(i*j)
    b = ''
    for k in range(len(a)-1,-1,-1):
      b += a[k]
    if b == a:
      c.append(int(b))
print('hasil palindrome dari perkalian tiga digit angka adalah',max(c))
