from Card import *

STARTING_CASH = 1000

class Player:
    def __init__(self, card1, card2, money, neuralNet):
        self.card1 = card1
        self.card2 = card2
        self.money = money
        self.moneyInPot = 0

        self.neuralNet = neuralNet
        self.numWins = 0

    def setCardOne(self, newCard):
        self.card1 = newCard

    def setCardTwo(self, newCard):
        self.card2 = newCard

    def setMoney(self, newMoney):
        self.money = newMoney
    
    def setMoneyInPot(self, newMoney):
        self.moneyInPot = newMoney
    
    def incrementWins(self):
        self.numWins += 1

    def resetWins(self):
        self.numWins = 0

        
    def setNeuralNet(self, neuralNet):
        self.neuralNet = neuralNet

    def getCardOne(self):
        return self.card1
    
    def getCardTwo(self):
        return self.card2

    def getMoney(self):
        return self.money

    def getMoneyInPot(self):
        return self.moneyInPot

    def getWins(self):
        return self.numWins

    def toString(self):
        return "Wins: ", self.numWins

    def getNeuralNet(self):
        return self.neuralNet

# Method which deals a card to a player.
def dealCard(player):
    card = getRandomCard()
    player.setCardOne(card)