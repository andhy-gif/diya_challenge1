kata=input('masukkan kata anda:')
hasil = ''
for i in kata:
    if i ==  'a':
        hasil += i
print('jumlah a pada {} adalah {}'.format(kata,len(hasil)))
