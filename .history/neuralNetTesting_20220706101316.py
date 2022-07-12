from NeuralNetwork import *
import torch

model = NeuralNetwork().to(device)
print(model)

x = torch.rand(1, 16)
logits = model(x)
prob = nn.Softmax(dim=1)(logits)
print (prob)
#print(logits)