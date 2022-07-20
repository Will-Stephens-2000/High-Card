from NeuralNetwork import *
import torch
from Player import *
device = "cuda" if torch.cuda.is_available() else "cpu"

model = NeuralNetwork().to(device)
print(model)

x = torch.rand(NUM_INPUTS)
logits = model(x)
prob = nn.Softmax(dim=1)(logits) # dim=1 is necessary to make probabilities sum to 1
y_pred = prob.argmax(1)
print (prob)
print(y_pred)
#print(logits)3

# #inputWeights = model.linear_relu_stack.parameters
# torch.save(model.state_dict(), 'weights_only.pth')
# #print(model.state_dict())
print(model.getWeights())
# model_new = NeuralNetwork()
# model_new.load_state_dict(torch.load('weights_only.pth'))
# logits = model_new(x)
# prob = nn.Softmax(dim=1)(logits) # dim=1 is necessary to make probabilities sum to 1
# y_pred = prob.argmax(1)
# print (prob)
# print(y_pred)
