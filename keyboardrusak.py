print ('MENGURUTKAN TEKS DAN MENGHAPUS TEKS YANG SAMA')
teks= input('teks anda:')
huruf = ''
kt_baru = ''
for i in range(len(teks)):
  if len(teks) != i+1:
    if teks[i] != teks[i+1]:
      kt_baru += teks[i]
  else:
    kt_baru += teks[i]
print(kt_baru)


  
