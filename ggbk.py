def gbk(x,y):
  p1 = '{}'.format(x)
  p2 = '{}'.format(y)
  if p1 == 'G':
    if p2 == 'G':
      return 0
    elif p2 == 'B':
      return 2
    else:
      return 1
  if p1 == 'B':
    if p2 == 'G':
      return 1
    elif p2 == 'B':
      return 0
    else:
      return 2
  if p1 == 'K':
    if p2 == 'G':
      return 2
    elif p2 == 'B':
      return 1
    else:
      return 0
import getpass
print('PERMAINAN GUNTING BATU KERTAS')
print('Ketikkan pilihan anda')
print('G untuk Gunting')
print('B untuk Batu')
print('K untuk kertas')
x = getpass.getpass(prompt='pemian 1:').upper()
if x != 'G' and x != 'B' and x != 'K':
  print('Pilihan anda tidak tersedia')
y = getpass.getpass(prompt='pemain 2:').upper()
if y != 'G' and y != 'B' and y != 'K':
  print('Pilihan anda tidak tersedia')
if gbk(x,y) == 1:
  print('Pemain 1 menang')
elif gbk(x,y) == 2:
  print('Pemain 2 menang')
elif gbk(x,y) == 0:
  print('Seri')
else:
  print('Pemain memasukkan pilihan yang salah')

