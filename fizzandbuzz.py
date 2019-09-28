a=int(input('masukkan angka anda:'))
for i in range(1,a+1):
  if i % 3 == 0:
    print(i,'fiiz')
  elif i % 5 == 0:
    print(i,'buzz')
  if i % 3 == 0 and i % 5 == 0:
    print(i,'fizzbuzz')
  else:
    print(i)
