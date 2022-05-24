from distutils.log import error
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    
    def getRank(self): 
        return self.rank

    def getSuit(self):
        return self.suit
    
    def toString(self):
        return (self.getRank() + self.getSuit())


    
    def compareRankTo(self, card):
        selfRank = int(convertRank(self.getRank()))
        cardRank = int(convertRank(card.getRank()))
        if (selfRank < cardRank):
            return -1

        elif int(selfRank == cardRank):
            return 0

        else:
            return 1


# Converts rank like A to its relevant integer value.
# The card's rank is not changed, just altered for the sake of rank comparision
# J -> 11
# Q -> 12
# K -> 13
# A -> 14 
# A might also return 1 but it is not yet implemented.
#
def convertRank(rank):
    if rank == "J":
        return "11"
    elif rank == "Q":
        return "12"
    elif rank == "K":
        return "13"
    elif rank == "A":
        return "14"
    else:
        return rank


# Method which returns a random card 
# We do not care about the suit at this time, so we do not care about the suit
# Since there are only two players, both players can have the same rank 
#   i.e. can't have five aces since we only have two players
def getRandomCard():
    rank = random.randint(2, 14)

    if rank <= 10:
        return Card(str(rank), "H")
    elif rank == 11:
        return Card("J", "H")
    elif rank == 12:
        return Card("Q", "H")
    elif rank == 13:
        return Card("K", "H")
    elif rank == 14:
        return Card("A", "H")  

    raise Exception("getRandomCard created a card with an impossible rank")