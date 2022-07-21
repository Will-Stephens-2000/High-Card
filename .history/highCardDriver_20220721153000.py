from Card import *
from Player import *
from NeuralNetwork import *

SMALL_BLIND_AMOUNT = 20
TURNS_FOR_BLIND_INCREASE = 5


def playHighCard(player1, player2):
    turn = 1
    bigBlindPosition = 1
    pot = 0
    while player1.getMoney() > 0 and player2.getMoney() > 0: # loop until a player wins
        pot = 0
        resetPot(player1, player2)
        dealCard(player1)
        dealCard(player2)

        print("\nNew Hand:\n")
        if bigBlindPosition == 1:
            turn = 2
            pot += insertBlind(player1, SMALL_BLIND_AMOUNT)
            player1.setMoneyInPot(SMALL_BLIND_AMOUNT)
            neededBetToCall = SMALL_BLIND_AMOUNT

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

                    pot = 0
                    resetPot(player1, player2)
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
                    
                    pot = 0
                    resetPot(player1, player2)
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
                    raise Exception("The player has made an unknown action")    
        
        else: # player2 is big blind
            turn = 1
            pot += insertBlind(player2, SMALL_BLIND_AMOUNT)
            player2.setMoneyInPot(SMALL_BLIND_AMOUNT)
            neededBetToCall = SMALL_BLIND_AMOUNT
            playerAction = (None, None)
            while playerAction[0] != "Fold" and playerAction[0] != "Call": # loop until someone calls or folds
                if turn == 1:
                    playerAction = action(player1, player2, neededBetToCall)
                    turn = 2
                else:
                    playerAction = action(player2, player1, neededBetToCall)
                    turn = 1


                # a player has folded, so the other gets the pot.
                # We've already changed turn above, so just check which turn,
                # payout, and reset.
                if playerAction[0] == "Fold": 
                    if turn == 1:
                        print("Fold. Player 1 Wins: ", pot)
                        player1.setMoney(player1.getMoney() + pot)
                    else:
                        print("Fold. Player 2 Wins: ", pot)
                        player2.setMoney(player2.getMoney() + pot)

                    pot = 0
                    resetPot(player1, player2)
                    bigBlindPosition = 1
                    continue

                elif playerAction[0] == "Call": 
                    print("Call: ", playerAction[1])
                    pot += playerAction[1]

                    if (player1.getMoneyInPot() - player2.getMoneyInPot() > 0.00000001):
                        print ("Player1 put in: ", player1.getMoneyInPot())
                        print ("Player2 put in: ", player2.getMoneyInPot())
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
                    
                    pot = 0
                    resetPot(player1, player2)
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
    
    if player1.getMoney() > 0:
        return player1
    else:
        return player2


def resetPot(player1, player2):
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
        player.setMoneyInPot(moneyLeft)
        return moneyLeft

    player.setMoney(player.getMoney() - amount)
    player.setMoneyInPot(amount)
    return amount
    

# The player indicates their action.
# The player can bet, call, raise, or fold.
# maybe return tuple with action (fold, call, raise, shove) and amount
# shove can be a faster way to raise all in, would still count as a raise
def action(decidingPlayer, otherPlayer, currentBet):
    print ("Your Card:", decidingPlayer.getCardOne().toString())
    print ("Amount needed to call: ", currentBet)
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
                otherPlayer.setMoney(otherPlayer.getMoney() + 
                    (currentBet - decidingPlayer.getMoney()))
                otherPlayer.setMoneyInPot(otherPlayer.getMoneyInPot() - 
                    (currentBet - decidingPlayer.getMoney()))
                
                decidingPlayer.setMoneyInPot(decidingPlayer.getMoneyInPot() + decidingPlayer.getMoney())
                decidingPlayer.setMoney(0)
                
                return ("Call", decidingPlayer.getMoney())
            
            decidingPlayer.setMoney(decidingPlayer.getMoney() - currentBet)
            decidingPlayer.setMoneyInPot(decidingPlayer.getMoneyInPot() + currentBet)
            return ("Call", currentBet)


        elif playerAction == "Raise" or playerAction == "raise" \
                or playerAction == "r" or playerAction == "R":
            
            raiseAmount = int(input("How much would you like to raise: (-1 to go back): "))
            

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


# A version of highCard for computer vs computer.
# We will call this method to get the outcome of each match of neural nets.

# player1 and player2 are Player objects
# 
def playHighCardCvC(player1, player2):
    print("new game against new players")
    turnsUntilBlind = TURNS_FOR_BLIND_INCREASE
    blindMultiplier = 1
    player1Big = True

    bigBlind = SMALL_BLIND_AMOUNT * blindMultiplier

    while(player1.getMoney() > 0 and player2.getMoney() > 0):
        print("player1 ", player1.getMoney(), " player2: ", player2.getMoney())
        if turnsUntilBlind == 0:
            blindMultiplier *= 2
            turnsUntilBlind = TURNS_FOR_BLIND_INCREASE

        bigBlind = SMALL_BLIND_AMOUNT * blindMultiplier

        #
        if player1Big:
            result = playHand(player2, player1, bigBlind)
            player2.setMoney(result[0])
            player1.setMoney(result[1])
            player1Big = False
        else:
            result = playHand(player1, player2, bigBlind)
            player1.setMoney(result[0])
            player2.setMoney(result[1])
            player1Big = True

        print(result)
        turnsUntilBlind -= 1


    if player1.getMoney() > 0 :
        return player1
    else:
        return player2


# smallBlind and bigBlind are player objects
# blindAmount is the smallBlind amount
def playHand(smallBlind, bigBlind, blindAmount):
    
    dealCard(smallBlind)
    dealCard(bigBlind)
    pot = 0
    print("\n\nNew Hand: SB:", smallBlind.getMoney(), " BB:", bigBlind.getMoney())
    print(blindAmount, 2 * blindAmount)
    # small blind player has less than small blind amount, so just have poorest player
    #   shove and the other matches. No betting since one player has shoved.
    if smallBlind.getMoney() <= blindAmount or bigBlind.getMoney() <= 2 * blindAmount:
        print("we have only a few chips left")
        chipsIn = min(smallBlind.getMoney(), bigBlind.getMoney())
        
        pot += insertBlind(smallBlind, chipsIn)
        pot += insertBlind(bigBlind, chipsIn)

        winner = getWinner(smallBlind, bigBlind)

        if winner == 0:
            pot -= chipsIn
            awardMoney(smallBlind, chipsIn)
        else:
            pot -= chipsIn
            awardMoney(bigBlind, chipsIn)
        resetPot(smallBlind, bigBlind)
        return (smallBlind.getMoney(), bigBlind.getMoney())
    else:
        pot += insertBlind(smallBlind, blindAmount)
        pot += insertBlind(bigBlind, 2 * blindAmount)
        #print("players' money after blinds:", smallBlind.getMoney(), bigBlind.getMoney())
        
        # action = 0 => smallBlind's action and action = 1 => bigBlind's action
        # action = -1 => someone called or folded
        action = 0
        betSize = 2 * blindAmount
        smallBlindWin = False
        bigBlindWin = False

        while action != -1:
            if action == 0: # smallBlind's turn
                decisions = botAction(smallBlind, betSize)
                myDecision = getFirstValidAction(smallBlind, decisions, betSize)
                print(myDecision[0], myDecision[1], "smallBlind")
                if myDecision[0] == "Fold":
                    bigBlindWin = True

                    break
                elif myDecision[0] == "Call":
                    # must refund
                    callAmount = myDecision[1]
                    print(callAmount)
                    
                    
                    pot = 2 * callAmount
                    smallBlind.setMoney(smallBlind.getMoney() - callAmount + smallBlind.getMoneyInPot())
                    smallBlind.setMoneyInPot(callAmount)


                    if bigBlind.getMoneyInPot() + smallBlind.getMoneyInPot() - pot > .01:
                        raise Exception("Players have not inserted equal amounts into the pot:",
                            "smallBlind: ", smallBlind.getMoneyInPot(), " bigBlind: ", bigBlind.getMoneyInPot(),
                             " pot: ", pot)

                    break
                
                # small blind can not call full amount, so we refund what's necessary 
                elif myDecision[0] == "Special Call":
                    callAmount = myDecision[1] + smallBlind.getMoneyInPot()

                    pot = 2 * callAmount

                    smallBlind.setMoney(0)
                    smallBlind.setMoneyInPot(callAmount)

                    bigBlind.setMoney(bigBlind.getMoney() + bigBlind.getMoneyInPot() - callAmount)
                    bigBlind.setMoneyInPot(callAmount)
                    break

                elif myDecision[0] == "Raise":
                    #print(myDecision[1])
                    raiseAmount = myDecision[1]

                    pot += raiseAmount #- smallBlind.getMoneyInPot()
                    #print(pot)
                    smallBlind.setMoney(smallBlind.getMoney() - raiseAmount + smallBlind.getMoneyInPot())
                    #print(smallBlind.getMoney())
                    betSize = raiseAmount #+ smallBlind.getMoneyInPot()
                    #print(betSize)
                    smallBlind.setMoneyInPot(raiseAmount)
                    #print(smallBlind.getMoneyInPot())
                    action = 1

            else: # bigBlind's turn
                decisions = botAction(bigBlind, betSize)
                myDecision = getFirstValidAction(bigBlind, decisions, betSize)
                print(myDecision[0], myDecision[1], "bigBlind")
                if myDecision[0] == "Fold":
                    smallBlindWin = True
                    break
                
                elif myDecision[0] == "Call":
                    callAmount = myDecision[1]
                    print("callAmount", callAmount)

                    pot = 2 * callAmount
                    bigBlind.setMoney(bigBlind.getMoney() - callAmount + bigBlind.getMoneyInPot())
                    bigBlind.setMoneyInPot(callAmount)
        
                    if bigBlind.getMoneyInPot() + smallBlind.getMoneyInPot() - pot > .01:
                        raise Exception("Players have not inserted equal amounts into the pot:",
                            "smallBlind: ", smallBlind.getMoneyInPot(), " bigBlind: ", bigBlind.getMoneyInPot(),
                            " pot: ", pot)
                    break
                
                # big blind can not call full amount, so we refund what's necessary 
                elif myDecision[0] == "Special Call":
                    callAmount = myDecision[1] + bigBlind.getMoneyInPot()

                    pot = 2 * callAmount

                    bigBlind.setMoney(0)
                    bigBlind.setMoneyInPot(callAmount)

                    smallBlind.setMoney(smallBlind.getMoney() + smallBlind.getMoneyInPot() - callAmount)
                    smallBlind.setMoneyInPot(callAmount)
                    break

                elif myDecision[0] == "Raise":
                    raiseAmount = myDecision[1]

                    pot += raiseAmount #- bigBlind.getMoneyInPot()
                    bigBlind.setMoney(bigBlind.getMoney() - raiseAmount + bigBlind.getMoneyInPot())
                    print (bigBlind.getMoney())
                    betSize = raiseAmount #+ bigBlind.getMoneyInPot()
                    bigBlind.setMoneyInPot(raiseAmount)
                                      
                    action = 0


        # if smallBlind.getMoneyInPot() - bigBlind.getMoneyInPot() > 0.000000001:
        #     raise Exception("Players have not inserted equal amounts into the pot:",
        #      "smallBlind: ", smallBlind.getMoneyInPot(), " bigBlind: ", bigBlind.getMoneyInPot())


        if smallBlindWin:
            print("small blind wins:", pot)
            awardMoney(smallBlind, pot)
        elif bigBlindWin:
            print("bigBlind wins:", pot)
            awardMoney(bigBlind, pot)
        else:
            winner = getWinner(smallBlind, bigBlind)

            if winner == 0:
                print("chop!", pot/2)
                awardMoney(smallBlind, pot/2)
                awardMoney(bigBlind, pot/2)
            elif winner == 1:
                print("small blind wins:", pot)
                awardMoney(smallBlind, pot -  blindAmount)
            else:
                print("big blind wins:", pot)
                awardMoney(bigBlind, pot)
        print(smallBlind.getMoney(), bigBlind.getMoney())
        resetPot(smallBlind, bigBlind)
        
        if smallBlind.getMoney() < 0 or bigBlind.getMoney() < 0:
            raise Exception("Someone's taken out a loan somehow", smallBlind.getMoney(), bigBlind.getMoney())
        if (smallBlind.getMoney() + bigBlind.getMoney()) > 2000.1:
            raise Exception("Infinite Money Glitch: More money is in the game than possible:",
                "smallBlind: ", smallBlind.getMoney(), " bigBlind: ", bigBlind.getMoney())
        if (smallBlind.getMoney() + bigBlind.getMoney()) < 1999.9:
            raise Exception("un-Infinite Money Glitch: Less money is in the game than possible:",
                "smallBlind: ", smallBlind.getMoney(), " bigBlind: ", bigBlind.getMoney())
    
    return (smallBlind.getMoney(), bigBlind.getMoney())


def validAction(action):
    validActions = ["Call", "call", "c", "C", "Raise", "raise", "r", "R", "Fold", "fold", "f", "Fold"]

    if action in validActions:
        return True
    
    return False


def getWinner(player1, player2):
    result = player1.getCardOne().compareRankTo(player2.getCardOne())

    # tie
    if result == 0:
        return 0

    # player 1 wins
    elif result == -1:
        return 1
    
    # player 2 wins
    else:
        return 2

def awardMoney(player, amount):
    player.setMoney(player.getMoney() + amount)
    player.setMoneyInPot(0)

def botAction(player, betSize):
    inputs = createInputs(player.getCardOne(), betSize, player.getMoney())
    #print(type(inputs))
    
    model = player.getNeuralNet()
    logits = model(inputs.float())
    possibleActions = nn.Softmax(dim=1)(logits)
    
    return possibleActions


def getFirstValidAction(player, actions, betSize):
    #print("length", len(actions[0]))
    sortedActions = torch.sort(actions, descending=True)[1]
    #print("sortedActions: ", sortedActions)
    #print(type(sortedActions))
    for i in range(0, len(actions[0])):
        
        # I don't know why the tensor is 2d, but i needed to access
        # the first tensor in listActions, hence listActions[0][maxIndex]
        possibleAction = sortedActions[0][i].item()
        #print("possibleAction", possibleAction)
        if possibleAction == 0: # fold
            #print("I should be folding")
            return ("Fold", 0)
        
        elif possibleAction == 1: #call
            if player.getMoney() + player.getMoneyInPot() < betSize:
                return ("Special Call", player.getMoney())            
            return ("Call", betSize)
        
        elif possibleAction == 2: #minRaise: will only return if a min raise is possible
            if player.getMoney() + player.getMoneyInPot() < 2 * betSize:
                #print("made it to continue")
                continue
            return ("Raise", betSize * 2)
        elif possibleAction == 3: # higherRaise: will only return if the raise amount is possible
            if player.getMoney() + player.getMoneyInPot() < 5 * betSize:
                #print("made it to continue")
                continue
            return ("Raise", 5 * betSize)
        else: # shove: put all remaining chips into the pot: if money < betSize: counts as call          
            if player.getMoney() <= betSize:
                print("shoving with less than bet")
                return ("Special Call", player.getMoney())
            return ("Raise", player.getMoney()) 
    
    raise Exception("All actions were invalid.")                    


# Plays a Round Robin bracket for each neural net.
# Tracks the number of wins for each neural net.
# Returns a list of neural nets sorted from most to least winning nets.
#
# neuralNets is a list of neuralNets
# returns a list of neuralNets sorted from most to least number of wins.
def playTournament(players):
    for i in range(len (players) - 1):
        for j in range(i+1, len(players)):
            player1 = players[i]
            player2 = players[j]
            player1.setMoney(STARTING_CASH)
            player2.setMoney(STARTING_CASH)

            winner = playHighCardCvC(player1, player2)
            
            if winner == player1:
                players[i].incrementWins()
            else:
                players[j].incrementWins()

    return sorted(players, key = lambda x:x.numWins, reverse=True)



NUM_PLAYERS = 10
def main():
    gen1Players = [None] * NUM_PLAYERS

    for i in range(NUM_PLAYERS):
        gen1Players[i] = Player(None, None, STARTING_CASH, NeuralNetwork().to("cpu"))

    winners = playTournament(gen1Players)

    for i in range(NUM_PLAYERS):
        #print(winners[i].getNeuralNet().getWeights())
        print(winners[i].toString())



if __name__ == "__main__":
    main()