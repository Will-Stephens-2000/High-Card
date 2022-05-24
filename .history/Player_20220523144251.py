from http.client import MOVED_PERMANENTLY


class Player:
    def __init__(self, card1, card2, money):
        self.card1 = card1
        self.card2 = card2
        self.money = money


    def getCardOne(self):
        return self.card1
    
    def getCardTwo(self):
        return self.card2

    def getMoney(self):
        return self.money


    