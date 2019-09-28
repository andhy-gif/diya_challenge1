def gan_gen(bilangan):
  '''
  fungsi ini akan mencetak apakah argumen yang dimasukkan bernilai ganjil atau genap
  '''
  if bilangan % 2 == 0:
    print('{} adalah bilangan genap'.format(bilangan))
  else:
    print('{} adalah bilangan ganjil'.format(bilangan))

def bil_bes(x,y,z):
  '''
  fungsi ini akan mencetak bilangan terbesar dari tiga argumen yang diberikan
  '''
  if x >= y and x >= z:
    print('{} adalah bilangan terbesar'.format(x))
  elif y >= x and y >= z:
    print('{} adalah bilangan terbesar'.format(y))
  else:
     print('{} adalah bilangan terbesar'.format(z))

bil_bes(1,2,3)
bil_bes(9,8,7)
bil_bes(6,7,5)
bil_bes(8,8,8)

