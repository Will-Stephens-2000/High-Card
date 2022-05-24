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