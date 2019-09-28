a=input('msukkan kata nada:')
kata_baru=''
for i in range(len(a)-1,-1,-1):
    kata_baru += a[i]
print('kebalikan kata {} adalah {}'.format(a,kata_baru))
