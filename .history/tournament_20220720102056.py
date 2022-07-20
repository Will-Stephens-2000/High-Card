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
def playTournament(neuralNets):
    numWins = {}
    for i in range(neuralNets):
        numWins[neuralNets[i]] = 0
        
    for i in range(len (neuralNets) - 1):
        for j in range(i+1, len(neuralNets)):
            player1 = Player(None, None, STARTING_CASH, neuralNets[i])
            player2 = Player(None, None, STARTING_CASH, neuralNets[j])

            winner = playHighCardCvC(player1, player2)