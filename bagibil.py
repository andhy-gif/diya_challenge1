print ('anda akan diminta memasukkan angka di bawah 100')
a =int(input('masukkan angka di sini :'))
if a >100:
  print ('angka yang anda masukkan terlalu besar')
else:
  for i in range(2,100):
    if a % i == 0:
      print (i)

      
