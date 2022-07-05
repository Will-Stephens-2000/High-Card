import torch
from torch import nn
from torch.utils.data import DataLoader

NUM_HIDDEN = 100
device = "cuda" if torch.cuda.is_available() else "cpu"



class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        
        self.flatten = nn.Flatten()
        
        self.linear_relu_stack = nn.Sequential(
            # 13 card ranks plus currBet, myChips, and opponentsChips as input
            nn.Linear(16, NUM_HIDDEN),
            nn.ReLU(),
            nn.Linear(NUM_HIDDEN, NUM_HIDDEN),
            nn.ReLU(),
            nn.Linear(NUM_HIDDEN, 5), # 5 outputs: fold, call minRaise, higherRaise, shove
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits