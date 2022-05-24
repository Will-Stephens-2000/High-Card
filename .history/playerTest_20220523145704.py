from Player import *
from Card import *

card1 = Card("4", "H")
card2 = Card("6", "H")
player1 = Player(card1, card2, 500)

print(player1.toString())


dealCard(player1)

print (player1.toString())