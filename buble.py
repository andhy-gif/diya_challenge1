'''
Fungsi berikut mengurutkan angka menggunakan algoritma bubble sort
'''
def bubble_sort(angka):
  for pos_tujuan in range(len(angka)-1,1,-1):
    for pos_skrg in range(pos_tujuan):
      if angka[pos_skrg] > angka[pos_skrg+1]:
        angka[pos_skrg],angka[pos_skrg+1] = angka[pos_skrg+1],angka[pos_skrg]
        

angka = [34,21,45,32,12,31,19,23,54,31,25,27]
print('sebelum sort:',angka)
bubble_sort(angka)
print('setelah sort:',angka)
