def kta(kata):
    vocal=['a','i','u','e','o']
    konsonan=0
    for i in kata:
        if i not in  vocal:
            konsonan += 1
        elif konsonan < 3:
            konsonan = 0
    if konsonan >= 3:
         return 'sulit'
    else:
         return 'mudah'

inp = int(input(':'))

for i in range(inp):
     a=input(':')
     print('{}->{}'.format(a, kta(a)))
        
