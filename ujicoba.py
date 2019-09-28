a,b,c,d = 1,'umar',90.0,'aku'
print (a)

#batas pembelajaran
z,x,c,v = 'subur',1,12.1,True
print(x, 'tipenya adalah', type(x))
print(z, 'tipenya adalah', type(z))
print(c, 'tipenya adalah', type(c))
print(v, 'tipenya adalah', type(v))

#batas pembelajaran
panjang = 100 # tipe data integer
lebar = 21.5 # tipe data float
nama = "Umar" # tipe string
print(panjang)
print(lebar)
print(nama)
print(panjang*lebar)

#batas pembelajaran
#belajar list

data = [1,2,3,4,5,6,'aku','marah',True,12.0]
print (data[0])
print(data[4])
print(data,[7])
print(len(data))

#batas pembelajaran
#string 

home = 'meja ini bundar'
print(home[1])
print(home[8])
print(home[10])

#batas pembelajaran
#list
body = ['mata',1,12.4,'aku','mending',12]
print (body[0])
print(body[:3])
print(body[2:])

#batas pembelajaran
#tuple 
white = (255,255,255,255)
red = (255,0,0)
print (white)
print(red)

#bats bahasan
#set fungsinya adalh menghilangkan variabel yang sama
my_set = {'aku',1,2,4,2,3,4,1}
print (my_set)
print (my_set)

#batas bahasan
#dictionary adalah data yang didalamnya harus ada key:value ditandai dengan kurung kurawal 

a = {1:'satu',2:'dua'}
print(a[1])
print(a[2])

#batas bahsan
#percabangan mengunakan fungsi f 





#latihan membuat mesin belanja dari fungsi if atau percabangan
a =("selamat datang di toko kami ini daftar harga dan barangnya kerupuk=1000 qoqa-qola=2000 fanta=3000 sprit=1000 mie goreng = 12000")
print (a)
b = input('masukkan total pembayaran anda:Rp.')
if b >= '1000':
  print ('selamat anda mendapatkan bonus uang tunai senilai Rp.100.000 karena belanja anda melebi batas kerja kami')
else:
  print ('mohon maaf total pembyaran anda kurang dari 1000000 ')
print ('total pembayaran anda andalah',b , 'terima kasih atas kunjungannya')

#latihan looping pengulangan
for i in range(10000):
  x = x+1
  print(x)

