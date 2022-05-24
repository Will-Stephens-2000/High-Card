import unittest
from card import *

class TestCardClass(unittest.TestCase):
    
    # Set up method which instantiates a card of each rank.
    # Suit is not relevant at this point, so only instantiate hearts
    #
    # to call a card object: self.twoH.doSomething()
    def setUp(self):
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
    
    def testToString(self):
        #nineH = Card("9", "H").toString()

        self.assertEqual(self.nineH.toString(), "9H")
        self.assertEqual(self.tenH.toString(), "10H")
        self.assertEqual(self.kingH.toString(), "KH")

    def testcompareRankTo(self):
        self.assertEqual(self.fiveH.compareRankTo(self.sixH), -1)
        self.assertEqual(self.nineH.compareRankTo(self.tenH), -1)
        self.assertEqual(self.tenH.compareRankTo(self.jackH), -1)
        self.assertEqual(self.jackH.compareRankTo(self.kingH), -1)
        self.assertEqual(self.kingH.compareRankTo(self.aceH), -1)

        self.assertEqual(self.fiveH.compareRankTo(self.fiveH), 0)
        self.assertEqual(self.jackH.compareRankTo(self.jackH), 0)
        self.assertEqual(self.aceH.compareRankTo(self.aceH), 0)
        
        
        self.assertEqual(self.threeH.compareRankTo(self.twoH), 1)    
        self.assertEqual(self.sevenH.compareRankTo(self.fourH), 1)
        self.assertEqual(self.jackH.compareRankTo(self.tenH), 1)
        self.assertEqual(self.kingH.compareRankTo(self.jackH), 1)
        self.assertEqual(self.aceH.compareRankTo(self.twoH), 1)
        self.assertEqual(self.aceH.compareRankTo(self.kingH), 1)


       
        

    
if __name__ == "__main__":
    unittest.main()