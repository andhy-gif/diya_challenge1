def main(koin):
  gambar=0
  angka=0
  for i in koin:
    if i ==1:
      gambar+=1
    else:
      angka+=1
  if gambar < angka:
    return gambar
  else:
    return angka
koin=[1,0,0,0,1,1,1,1,0]
print(main(koin))
