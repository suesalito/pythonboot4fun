


print ('Welcome to Tic Tac Toe')



newgame = 1
while(newgame==1):

    if newgame ==1:
        l = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        def checkwin():
            if newgame == 1:
                return False
            else:
                if (((l[0] == l[1] == l[2]) and (l[0] != ' '))
                or ((l[3] == l[4] == l[5]) and (l[3] != ' '))
                or ((l[6] == l[7] == l[8]) and (l[6] != ' '))
                or ((l[0] == l[3] == l[6]) and (l[0] != ' '))
                or ((l[1] == l[4] == l[7]) and (l[1] != ' '))
                or ((l[2] == l[5] == l[8]) and (l[2] != ' '))
                or ((l[0] == l[4] == l[8]) and (l[0] != ' '))
                or ((l[2] == l[4] == l[6]) and (l[2] != ' '))):
                    return True
                else:
                    return False


        print('|---|---|---|')
        print('| {l0} | {l1} | {l2} |'.format(l0=l[0], l1=l[1], l2=l[2]))
        print('|---|---|---|')
        print('| {l3} | {l4} | {l5} |'.format(l3=l[3], l4=l[4], l5=l[5]))
        print('|---|---|---|')
        print('| {l6} | {l7} | {l8} |'.format(l6=l[6], l7=l[7], l8=l[8]))
        print('|---|---|---|')

        round = 1
        while (round <= 9):
            newgame = 0


            if (round % 2 == 1):
                print ('X turn please select position :')
                move = input()
                l[int(move)-1] = 'X'
                #print (l)
            else:
                print('O turn please select position :')
                move = input()
                l[int(move)-1] = 'O'
                #print (l)

            print('|---|---|---|')
            print('| {l0} | {l1} | {l2} |'.format(l0= l[0],l1=l[1],l2=l[2]))
            print('|---|---|---|')
            print('| {l3} | {l4} | {l5} |'.format(l3=l[3], l4=l[4], l5=l[5]))
            print('|---|---|---|')
            print('| {l6} | {l7} | {l8} |'.format(l6=l[6], l7=l[7], l8=l[8]))
            print('|---|---|---|')


            #print (checkwin())
            if checkwin() == True:
                if (round % 2 == 1): print ('X wins the game.')
                if (round % 2 == 0): print('O wins the game.')
                break
            round += 1


        print ('Continue? 1:OK 2:Exit')
        reset = input()
        newgame = int(reset)

else:
    print('Thanks for playing')

