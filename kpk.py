print('Mencari Kelipatan Persekutuan Terkecil (KPK) dari dua bilangan')
bil1 = int(input('Masukkan bilangan pertama '))
bil2 = int(input('Masukkan bilangan kedua '))
kpk_ketemu = False
calon_kpk = 0
while not kpk_ketemu:
  calon_kpk = calon_kpk + bil1
  if calon_kpk % bil2 == 0:
    kpk_ketemu = True
    print('KPK dari bilangan {} dan {} adalah {}'.format(bil1,bil2,calon_kpk))
  else:
    print('{} bukan merupakan KPK {} dan {}'.format(calon_kpk,bil1,bil2))

  
