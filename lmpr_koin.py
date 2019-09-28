n=int(input('masukkan disini:'))
hasil=[]
for i in range(n):
  koin=int(input('masukkan sisi koin anda:'))
  hasil.append(koin)
gambar=0
angka=0
for i in hasil:
  if i ==1:
    gambar+=1
  else:
    angka+=1
if gambar < angka:
  print(gambar)
else:
  print(angka)
