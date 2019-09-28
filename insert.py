'''
Fungsi berikut mengurutkan angka menggunakan algoritma insertion sort
'''
def insertion_sort(angka):
  for pos_sekarang in range(1,len(angka)):
    pos_sisip = pos_sekarang
    while angka[pos_sisip] < angka[pos_sisip-1] and pos_sisip>0:
      angka[pos_sisip],angka[pos_sisip-1] = angka[pos_sisip-1],angka[pos_sisip]
      pos_sisip = pos_sisip -1
          
angka = [34,21,45,32,12,31,19,23,54,31,25,27]
print('sebelum sort:',angka)
insertion_sort(angka)
print('setelah sort:',angka)


# animasi https://en.wikipedia.org/wiki/File:Insertion-sort-example-300px.gif
