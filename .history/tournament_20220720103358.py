from Card import *
from Player import *
from highCardDriver import *
from NeuralNetwork import *
import torch
from torch import nn
import numpy as np



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

            winner = playHighCardCvC(player1, player2)

            winner.incrementWins()

    return sorted(players, key = lambda x:x.numWins, reverse=True)