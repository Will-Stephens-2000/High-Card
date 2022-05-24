class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    
    def getRank(self): 
        return self.rank

    def getSuit(self):
        return self.suit
    
    def toString(self):
        print (self.getRank() + self.getSuit())


    
    def compareRankTo(self, card):

        if (int(self.getRank()) > int(card.getRank())):
            return -1

        elif int(self.getRank()) == int(card.getRank()):
            return 0

        else:
            return 1

# Converts rank like A to its relevant integer value.
# J -> 11
# Q -> 12
# K -> 13
# A -> 14
def convertRank()