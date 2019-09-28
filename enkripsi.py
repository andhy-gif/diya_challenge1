a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b =input('masukkan pesan yang akan dienkripsi:')
c =b.lower()
hasil = ''
for i in c:
  if i in a:
    huruf_lama = a.index(i)
    huruf_baru = (huruf_lama + 13 ) % len(a)
    abjad_baru = a[huruf_baru]
    hasil += abjad_baru 
  else:
    hasil += ' ' 
print(hasil)
