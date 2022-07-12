from NeuralNetwork import *
import torch
import unittest
from Card import *
import numpy as np



class TestNeuralNetwork(unittest.TestCase):
    def setUp(self):
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
        check = np.zeros(NUM_INPUTS)
        check[0] = 1
        self.assertTrue(torch.equal(createInputs(self.twoH), torch.from_numpy(check)))


        check = np.zeros(NUM_INPUTS)
        check[12] = 1
        self.assertTrue(torch.equal(createInputs(self.aceH), torch.from_numpy(check)))


if __name__ == "__main__":
    unittest.main()