class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit



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
