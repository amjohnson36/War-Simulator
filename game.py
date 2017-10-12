import random
import time

from check_deck import checkDeck

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

suits = ['hearts', 'diamonds', 'spades', 'clubs']

deck = [Card(value, suit) for value in range(2, 15) for suit in suits]

random.shuffle(deck)

player1 = deck[0:26]
player2 = deck[26:52]

def checkDeck(player1, player2):
    for i in range(len(player1)):
        print("{0}: {1} of {2}".format(i, player1[i].value, player1[i].suit))
        input('')

    for i in range(len(player2)):
        print("{0}: {1} of {2}".format(i, player2[i].value, player2[i].suit))
        input('')

checkDeck(player1, player2)

p1name = input('What is your name, player 1? ')
p2name = input('What is your name, player 2? ')

ans = input('Do you want the dramatic countdown for war? (y/n) ')
ans1 = input('Do you want to be able to see cards left? (y/n) ')

running = input("Press enter to begin. ")
turns = 0

def printResults(name, value, suit):
    if value <= 10:
        print("{0}: {1} of {2}".format(name, value, suit))    
    
    elif value == 11:   
        print("{0}: Jack of {1}".format(name, suit))    

    elif value == 12:   
        print("{0}: Queen of {1}".format(name, suit))    

    elif value == 13:   
        print("{0}: King of {1}".format(name, suit))

    elif value == 14:   
        print("{0}: Ace of {1}".format(name, suit))

while player1 and player2:
    top = 0
    
    printResults(p1name, player1[top].value, player1[top].suit)
    printResults(p2name, player2[top].value, player2[top].suit)

    p1card = player1[top].value
    p2card = player2[top].value

    if p1card > p2card:
        player1.append(player2.pop(top))
        player1.append(player1.pop(top))
        print("{0} wins!\n".format(p1name))
        turns += 1

    elif p1card < p2card:
        player2.append(player1.pop(top))
        player2.append(player2.pop(top))
        print("{0} wins!\n".format(p2name))
        turns += 1

    elif p1card == p2card:
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

    if ans1 == 'y':
        print("{0}'s cards left: ".format(p1name) + str(len(player1)))
        print("{0}'s cards left: ".format(p2name) + str(len(player2)))
        print('')

    if running == 'y':
        pass

    else:
        running = input("Press enter to proceed (y to autosim). ")

if player1:
    print("\n\nCongrats {0}, you win! ".format(p1name))

if player2:
    print("\n\nContrats {0}, you win! ".format(p2name))

print("That game took {0} turns! ".format(turns))
