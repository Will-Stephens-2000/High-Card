from Card import *
from Player import *


BIG_BLIND_AMOUNT = 20

def playHighCard(player1, player2):
    turn = 1
    bigBlindPosition = 1

    while player1.getMoney() > 0 and player2.getMoney() > 0: # loop until a player wins
        resetPot(pot, player1, player2)
        dealCard(player1)
        dealCard(player2)

        if bigBlindPosition == 1:
            turn = 2
            pot += insertBlind(player1, BIG_BLIND_AMOUNT)
            player1.setMoneyInPot(BIG_BLIND_AMOUNT)
            neededBetToCall = BIG_BLIND_AMOUNT

            playerAction = (None, None)
            while playerAction[0] != "Fold" and playerAction[0] != "Call": # loop until someone calls or folds
                if turn == 1:
                    playerAction = action(player1, player2, neededBetToCall)
                    turn = 2
                else:
                    playerAction = action(player2, player1, neededBetToCall)
                    turn = 1


                # the a player has folded, so the other gets the pot.
                # We've already changed turn above, so just check which turn,
                # payout, and reset.
                if playerAction[0] == "Fold": 
                    if turn == 1:
                        print("Fold. Player 1 Wins: ", pot)
                        player1.setMoney(player1.getMoney() + pot)
                    else:
                        print("Fold. Player 2 Wins: ", pot)
                        player2.setMoney(player2.getMoney() + pot)

                    resetPot(pot, player1, player2)
                    bigBlindPosition = 2
                    continue

                elif playerAction[0] == "Call": 
                    print("Call: ", playerAction[1])
                    pot += playerAction[1]
                    
                    if (player1.getMoneyInPot() - player2.getMoneyInPot() > 0.00000001):
                        print ("Player1 pot: ", player1.getMoneyInPot())
                        print ("Player2 pot: ", player2.getMoneyInPot())
                        raise Exception("Error: players have not inputted equal amounts into the pot")
                        
                    print("Player 1: ", player1.getCardOne().getRank())
                    print("Player 2: ", player2.getCardOne().getRank())

                    higher = player1.getCardOne().compareRankTo(player2.getCardOne())

                    if higher == 1:
                        print("Player 1 wins ", pot)
                        player1.setMoney(player1.getMoney() + pot)
                    elif higher == 0:
                        print("Tie. Each player gets ", pot/2)
                        player1.setMoney(player1.getMoney() + pot/2)
                        player2.setMoney(player2.getMoney() + pot/2)
                    elif higher == -1:
                        print("Player 2 wins ", pot)
                        player2.setMoney(player2.getMoney() + pot)
                    else:
                        raise Exception("card comparision failed.")
                    
                    resetPot(pot, player1, player2)
                    bigBlindPosition = 2
                    continue

                elif playerAction[0] == "Raise":
                    print("Raise: ", playerAction[1])
                    pot += playerAction[1]
                    
                    if turn == 1: # player 2 just raised, so get player one's money in pot
                        neededBetToCall = player2.getMoneyInPot() - player1.getMoneyInPot()
                    else:
                        neededBetToCall = player1.getMoneyInPot() - player2.getMoneyInPot()
                
                else:
                    raise Exception("The player has made an unkonwn action")    
        
        else:
            turn = 1
            pot += insertBlind(player2, BIG_BLIND_AMOUNT)
            neededBetToCall = BIG_BLIND_AMOUNT
            playerAction = (None, None)
            while playerAction[0] != "Fold" and playerAction[0] != "Call": # loop until someone calls or folds
                if turn == 1:
                    playerAction = action(player1, player2, neededBetToCall)
                    turn = 2
                else:
                    playerAction = action(player2, player1, neededBetToCall)
                    turn = 1


                # the a player has folded, so the other gets the pot.
                # We've already changed turn above, so just check which turn,
                # payout, and reset.
                if playerAction[0] == "Fold": 
                    if turn == 1:
                        print("Fold. Player 1 Wins: ", pot)
                        player1.setMoney(player1.getMoney() + pot)
                    else:
                        print("Fold. Player 2 Wins: ", pot)
                        player2.setMoney(player2.getMoney() + pot)

                    resetPot(pot, player1, player2)
                    bigBlindPosition = 1
                    continue

                elif playerAction[0] == "Call": 
                    print("Call: ", playerAction[1])
                    pot += playerAction[1]

                    print("Player 1: ", player1.getCardOne().getRank())
                    print("Player 2: ", player2.getCardOne().getRank())

                    higher = player1.getCardOne().compareRankTo(player2.getCardOne())

                    if higher == 1:
                        print("Player 1 wins ", pot)
                        player1.setMoney(player1.getMoney() + pot)
                    elif higher == 0:
                        print("Tie. Each player gets ", pot/2)
                        player1.setMoney(player1.getMoney() + pot/2)
                        player2.setMoney(player2.getMoney() + pot/2)
                    elif higher == -1:
                        print("Player 2 wins ", pot)
                        player2.setMoney(player2.getMoney() + pot)
                    else:
                        raise Exception("card comparision failed.")
                    
                    resetPot(pot, player1, player2)
                    bigBlindPosition = 1
                    continue

                elif playerAction[0] == "Raise":
                    print("Raise: ", playerAction[1])
                    pot += playerAction[1]
                    
                    if turn == 1: # player 2 just raised, so get player one's money in pot
                        neededBetToCall = player2.getMoneyInPot() - player1.getMoneyInPot()
                    else:
                        neededBetToCall = player1.getMoneyInPot() - player2.getMoneyInPot()
                else:
                    raise Exception("The player has made an unkonwn action")                    


def resetPot(pot, player1, player2):
    pot = 0
    player1.setMoneyInPot(0)
    player2.setMoneyInPot(0)


# Method which subtracts the big blind from the player's balance.
# If the player has less than the blind amount, their balance goes to 0
# 
# @return the amount the player put in for the blind.
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
# maybe return tuple with action (fold, call, raise, shove) and amount
# shove can be a faster way to raise all in, would still count as a raise
def action(decidingPlayer, otherPlayer, currentBet):
    print ("Your Card:", decidingPlayer.getCardOne().toString())
    print ("The current bet is ", currentBet)
    print ("Your chips: ", decidingPlayer.getMoney())
    print ("Opponent's chips: ", otherPlayer.getMoney())
    playerAction = None

    while (not validAction(playerAction)):

        playerAction = input("Would you like to Call, Raise, or Fold ")

        if playerAction == "Call" or playerAction == "call" \
                or playerAction == "c" or playerAction == "C":

            # deciding player must go all in to call
            if decidingPlayer.getMoney() < currentBet:
                # if the bet is 20 and deciding player has 13, the bet becomes 13 and other player is refunded 20 - 13 = 7
                otherPlayer.setMoney(otherPlayer.getMoney() + (currentBet - decidingPlayer.getMoney()))
                otherPlayer.setMoneyInPot(otherPlayer.getMoneyInPot() - (currentBet - decidingPlayer.getMoney()))
                return ("Call", decidingPlayer.getMoney())
            
            decidingPlayer.setMoney(decidingPlayer.getMoney() - currentBet)
            decidingPlayer.setMoneyInPot(decidingPlayer.getMoneyInPot() + currentBet)
            return ("Call", currentBet)


        elif playerAction == "Raise" or playerAction == "raise" \
                or playerAction == "r" or playerAction == "R":
            
            raiseAmount = int(input("How much would you like to raise:"))
            while (raiseAmount < currentBet * 2):
                print ("Raise amount must be at least 2x the current bet.")
                raiseAmount = int(input("How much would you like to raise:"))

            if raiseAmount > decidingPlayer.getMoney():
                print("Raise amount is higher than current balance. \
                        Raising for", decidingPlayer.getMoney(), "instead.")
                raiseAmount = decidingPlayer.getMoney()
                decidingPlayer.setMoney(0)
                decidingPlayer.setMoneyInPot(decidingPlayer.getMoneyInPot() + raiseAmount)
                return ("Raise", raiseAmount)

                    
            decidingPlayer.setMoney(decidingPlayer.getMoney() - raiseAmount)
            decidingPlayer.setMoneyInPot(decidingPlayer.getMoneyInPot() + raiseAmount)
            return ("Raise", raiseAmount)
        
        elif playerAction == "Fold" or playerAction == "fold" \
                or playerAction == "f" or playerAction == "F":
            return ("Fold", 0)

        else:
            print("Invalid action: please Call, Raise, or Fold")


def validAction(action):
    validActions = ["Call", "call", "c", "C", "Raise", "raise", "r", "R", "Fold", "fold", "f", "Fold"]

    if action in validActions:
        return True
    
    return False





def main():
    player1 = Player(None, None, 1000)
    player2 = Player(None, None, 1000)
    playHighCard(player1, player2)




if __name__ == "__main__":
    main()