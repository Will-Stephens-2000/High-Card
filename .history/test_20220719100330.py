from NeuralNetwork import *
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

model = NeuralNetwork().to(device)
print(model)

x = torch.rand(1, NUM_INPUTS)
logits = model(x)
prob = nn.Softmax(dim=1)(logits) # dim=1 is necessary to make probabilities sum to 1
y_pred = prob.argmax(1)
print (prob)
print(y_pred)
#print(logits)3