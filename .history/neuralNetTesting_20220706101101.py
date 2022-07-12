from NeuralNetwork import *
import torch

model = NeuralNetwork().to(device)
print(model)

x = torch.rand(1, 16)
print(x)