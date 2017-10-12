import random
import time

from check_deck import checkDeck
from card import *
from war import war

# Creates deck, then shuffles and splits it into two decks each with 26 cards
suits = ['hearts', 'diamonds', 'spades', 'clubs']

deck = [Card(value, suit) for value in range(2, 15) for suit in suits]

random.shuffle(deck)

player1 = deck[0:26]
player2 = deck[26:52]

# checkDeck(player1, player2)

p1name = input('What is your name, player 1? ')
p2name = input('What is your name, player 2? ')

ans = input('Do you want the dramatic countdown for war? (y/n) ')
ans1 = input('Do you want to be able to see cards left? (y/n) ')

running = input("Press enter to begin. ")
turns = 0

# Main loop for the game. Proceeds while player1 and player2 both have cards within deck.

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
        war(player1, player2, p1card, p2card, p1name, p2name, top, turns, ans)
        
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
