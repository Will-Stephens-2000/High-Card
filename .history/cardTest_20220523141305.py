import unittest
from card import *

class TestCardClass(unittest.TestCase):
    
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

if __name__ == "__main__":
    unittest.main()