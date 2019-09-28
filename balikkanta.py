balik =input('masukkan kata anda: ')
string= ''
for i in range(len(balik)-1,-1,-1):
  string += balik[i]
print('kebalikan kata : {}'.format(string))


