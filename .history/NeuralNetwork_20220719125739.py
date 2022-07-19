import numpy as np
import torch
from torch import nn
from Card import *
from Player import *

NUM_INPUTS = 15 # 13 card ranks plus currBet and myChips as input
NUM_HIDDEN = 15
NUM_OUTPUTS = 5 # 5 outputs: fold, call minRaise, higherRaise, shove



# does bias count for next layer or current layer?
# if counts for next: must make bias false for final layer
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        
        self.flatten = nn.Flatten()
        
        self.linear_relu_stack = nn.Sequential(
            
            nn.Linear(NUM_INPUTS, NUM_HIDDEN),
            nn.ReLU(),
            nn.Linear(NUM_HIDDEN, NUM_HIDDEN),
            nn.ReLU(),
            nn.Linear(NUM_HIDDEN, NUM_OUTPUTS), 
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits



# this method activates the node which cooresponds to the current
# card rank and returns a tensor as such.
# This method does not currently take into account the nodes for betSize and chipSize
def createInputs(card, betSize, myChips):
    inputs = np.zeros(NUM_INPUTS)

    rank = int(convertRank(card.getRank()))
    
    #inputs[0] => rank = 2
    #inputs[12] => rank = 14 = A 
    inputs[rank-2] = 1

    total = float(myChips + betSize)
    inputs[13] = min(float(betSize/myChips), 1) # current bet
    inputs[14] = min(float(.5 * (myChips/STARTING_CASH)), 1) # myChips

    return torch.from_numpy(inputs)
