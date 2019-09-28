kalimat= input('masukkan kata:')
hasil = ''
for i in range(len(kalimat)-1,-1,-1):
  hasil += kalimat[i]
print('kebalikan dari {} adalah {}'.format(kalimat,hasil) )
print('{} merupakan palindrome'.format(hasil))


