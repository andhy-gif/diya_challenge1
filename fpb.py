print ('aplikasi pencarian fpb')
x =int(input('masukkan angka pertama anda: '))
y =int(input('masukkan angka kedua anda: '))
fpb = None
if x > y:
  kecil = y
else:
  kecil = x
for i in range(1,kecil + 1):
    if ((x % i == 0 and (y % i == 0))):
      fpb = i
if fpb == None:
  print('angka anda terlalu banyak')
else:
  print(fpb)
