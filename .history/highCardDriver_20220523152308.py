from Card import *
from Player import *

def playHighCard(player1, player2):
    turn = 1

    while player1.getMoney > 0 and player2.getMoney > 0:
        dealCard(player1)
        dealCard(player2)

        if turn == 1:
            action(player1)


def insertBlind(player, amount):

    # if player balance is less than big blind,
    # put in the entire player's stack
    if player.getMoney() < amount:
        player.setMoney(0)
        return player.getMoney()

    player.setMoney(player.getMoney() - amount)
    return amount
    

# The player indicates their action.
# The player can bet, call, raise, or fold.
def action(player):
    return -1


