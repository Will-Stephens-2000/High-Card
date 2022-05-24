from Card import *
from Player import *

def playHighCard(player1, player2):
    turn = 1

    while player1.getMoney > 0 and player2.getMoney > 0:
        pot = 0

        dealCard(player1)
        dealCard(player2)

        if turn == 1:
            action(player1)

# Method which subtracts the big blind from the player's balance.
# If the player has less than the blind amount, their balance goes to 0
# 
# @return the amount the player put in for the blind
def insertBlind(player, amount):

    # if player balance is less than big blind,
    # put in the entire player's stack
    if player.getMoney() < amount:
        moneyLeft = player.getMoney()
        player.setMoney(0)
        return moneyLeft

    player.setMoney(player.getMoney() - amount)
    return amount
    

# The player indicates their action.
# The player can bet, call, raise, or fold.
def action(player):
    return -1


