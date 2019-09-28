f = open('angka.txt')
teks = f.read(12) # membaca 27 karakter pertama pada posisi pembacaan saat ini
print(teks) 
print('------------') # cetak pembatas
f.seek(0,0) # mengembalikan posisi pembacaan ke awal
teks = f.read() # membaca seluruh isi file  
print(teks) 
f.close() # tutup file object setelah selesai digunakan
08 02 22 97 
49 49 99 40 
81 49 31 73 
52 70 95 23 n
