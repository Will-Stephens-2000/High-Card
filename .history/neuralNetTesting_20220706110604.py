from NeuralNetwork import *
import torch
import unittest




class TestNeuralNetwork(unittest.TestCase):
    def setup(self):
        #self.model = NeuralNetwork().to(device)
        #print(model)


        self.twoH = Card("2", "H")
        self.threeH = Card("3", "H")
        self.fourH = Card("4", "H")
        self.fiveH = Card("5", "H")
        self.sixH = Card("6", "H")
        self.sevenH = Card("7", "H")
        self.eightH = Card("8", "H")
        self.nineH = Card("9", "H")
        self.tenH = Card("10", "H")
        self.jackH = Card("J", "H")
        self.queenH = Card("Q", "H")
        self.kingH = Card("K", "H")
        self.aceH = Card("A", "H")

        #print(logits)
    
    def testCreateInputs(self):

        self.assertTrue(torch.equal(createInputs(self.twoH), torch.tensor([1,0,0,0,0,0,0,0,0,0,0,0,0])))



if __name__ == "__main__":
    unittest.main()