def checkDeck(player1, player2):
    for i in range(len(player1)):
        print("{0}: {1} of {2}".format(i+1, player1[i].value, player1[i].suit))
        input('')

    for i in range(len(player2)):
        print("{0}: {1} of {2}".format(i+1, player2[i].value, player2[i].suit))
        input('')
