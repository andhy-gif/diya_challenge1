kalimat =input('masukkan kata  anda:')
hasil = ''
for i in kalimat:
  if i == 'a':
    hasil += i
print('jumlah huruf a pad akalimat adlah {}'.format(len(hasil)))
