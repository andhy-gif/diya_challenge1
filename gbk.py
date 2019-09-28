player1=input('masukkan pilihan anda player 1:')
player2=input('masukkan pilihan anda player 2:')
if player1=='b' and  player2=='g':
    return 1
elif player1=='g' and player2=='b':
    return 2
elif player1=='k' and player2=='b':
    return 1
elif player1=='b' and player2=='k':
    return 2
elif player1=='g' and player2=='k':
    return 1
elif player1=='k' and player2=='g':
    return 2
elif player1==player2:
    return 0

            


        
        
