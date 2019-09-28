f = open('kata.txt')
l = f.readlines()
c = []
h=0
for i in l:
  c.append(i.rstrip().split(' '))
for i in range(len(c)):
  if c[i] == ['']:
    continue
  for j in c[i]:
    a = j
    b = ''
    for k in range(len(j)-1,-1,-1):
      b+=j[k]
    if a==b:
      h+=1
print(h)
Banyak peserta yang kasak kusuk ketika mengikuti perkemahan pada malam Minggu kanak alila
