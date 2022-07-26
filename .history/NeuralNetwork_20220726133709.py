import numpy as np
import random
import torch
from torch import nn
from Card import *
from Player import *

NUM_INPUTS = 15 # 13 card ranks plus currBet and myChips as input
NUM_HIDDEN = 15 # hyperparameter: chosen currently as 2/3 * NUM_INPUTS + NUM_OUTPUTS
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

    
    def setWeights(self, newWeights):
        for key in list(newWeights.keys()):
            self.state_dict()[key] = newWeights[key]


    # Method which returns an ordered dictionary containing
    # all weights with their cooresponding key values representing 
    # the names of each layer.
    def getWeights(self):
        return self.state_dict()





# Crossover strategy involving taking the average of each weight
# from both weight tensors
#
# weights1 and weights2 are ordered dictionaries
#   whose key values are the names of each layer
#   and values are a 2d list containing floats [0, 1].
#   
# Returns an orderd dictionary with the same keys mapped to 
# new averaged weight values.
def avgCrossover(weights1, weights2):
    finalDict = {}
    for key in sorted(weights1.keys()):
        #print(key)
        #print(weights1[key].size())
        tensor1 = weights1[key].tolist()
        tensor2 = weights2[key].tolist()
        
        #print(tensor1)
        
        biasWeights = isinstance(tensor1[0], float)

        if biasWeights:
            mutatedTensor = [0] * len(tensor1)
            for i in range(len(mutatedTensor)):
                w1 = tensor1[i]
                w2 = tensor2[i]
                mutatedTensor[i] = (w1 + w2)/2
        else:
            
            cols = len(tensor1[0])
            rows = len(tensor1)
            mutatedTensor = [[0]*cols for _ in range(rows)]

            for i in range(rows):
                for j in range(cols):
                    w1 = tensor1[i][j]
                    w2 = tensor2[i][j]
                    mutatedTensor[i][j] = (w1 + w2)/2

        finalDict[key] = torch.FloatTensor(mutatedTensor)
    
    return finalDict

# Method which adds a mutation to each weight if a random float [0,1) <= mutChance
# If this condition is met, a new float [-1, 1) is multiplied by mutStr
# and is added to the original weight.
#
# Returns an ordered dict which contains the new weights, both mutated and
#   unmutated.
def randomMutation(weightDict, mutStr, mutChance):
    finalDict = {}

    for key in sorted(weightDict.keys()):

        tensor = weightDict[key].tolist()
        biasWeights = isinstance(tensor[0], float)
        
        if biasWeights:
            mutatedTensor = [0] * len(tensor)
            for i in range(len(tensor)):
                if random.random() <= mutChance:
                    mutAmount = random.uniform(-1, 1) * mutStr
                    newWeight = tensor[i] + mutAmount
                    
                    mutatedTensor[i] = newWeight
        
        else:
            cols = len(tensor[0])
            rows = len(tensor)
            mutatedTensor = [[0]*cols for _ in range(rows)]
            
            for i in range (rows):
                for j in range(cols):
                    if random.random() <= mutChance:
                        mutAmount = random.uniform(-1, 1) * mutStr
                        newWeight = tensor[i][j] + mutAmount
                        
                        mutatedTensor[i][j] = newWeight

        finalDict[key] = torch.FloatTensor(mutatedTensor)
    
    return finalDict

# this method activates the node which cooresponds to the current
# card rank, activates nodes reflective of the current bet size 
# and the player's current chips and returns a tensor reflecting the activations.
def createInputs(card, betSize, myChips):
    inputs = np.zeros((1, NUM_INPUTS))

    rank = int(convertRank(card.getRank()))
    
    #inputs[0] => rank = 2
    #inputs[12] => rank = 14 = A 
    inputs[0][rank-2] = float(1.)

    #total = float(myChips + betSize)
    if myChips == 0:
        inputs[0][13] = 1
    else:
        inputs[0][13] = min(float(betSize/myChips), 1.) # current bet
    
    inputs[0][14] = min(float(.5 * (myChips/STARTING_CASH)), 1.) # myChips

    #print(inputs)
    return torch.from_numpy(inputs)
