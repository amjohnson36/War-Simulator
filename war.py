import time

def war(player1, player2, p1card, p2card, p1name, p2name, top, turns, ans):
    while p1card == p2card:
            print("War!\n")
            if ans == 'y':
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(1)

            top = top + 3
            turns += 1

            try:
                printResults(p1name, player1[top].value, player1[top].suit)
            except IndexError:
                for i in range(len(player1)):
                    player2.append(player1.pop(i))
                break

            try:            
                printResults(p2name, player2[top].value, player2[top].suit)
            except IndexError:
                for i in range(len(player2)):
                    player1.append(player2.pop(i))
                break

            p1card = player1[top].value
            p2card = player2[top].value

            if p1card > p2card:
                for i in range(0, top + 1):
                    try:
                        player1.append(player2.pop(0))
                        player1.append(player1.pop(0))
                    except IndexError:
                        break

                print("{0} wins!\n".format(p1name))

            elif p1card < p2card:
                for i in range(0, top + 1):
                    try:
                        player2.append(player1.pop(0))
                        player2.append(player2.pop(0))
                    except IndexError:
                        break

                print("{0} wins!\n".format(p2name))

