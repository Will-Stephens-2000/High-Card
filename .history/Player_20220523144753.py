from os import getrandom
import Card


class Player:
    def __init__(self, card1, card2, money):
        self.card1 = card1
        self.card2 = card2
        self.money = money


    def setCardOne(self, newCard):
        self.card1 = newCard

    def setCardTwo(self, newCard):
        self.card2 = newCard

    def getCardOne(self):
        return self.card1
    
    def getCardTwo(self):
        return self.card2

    def getMoney(self):
        return self.money


# Method which deals a card to a player.
def dealCard(player):
    card = Card.getRandomCard()
    player.setCardOne()