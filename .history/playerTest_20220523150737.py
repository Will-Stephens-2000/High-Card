from Card import *
from Player import *
import unittest


class testPlayerClass(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("4", "H")
        self.card2 = Card("6", "H")
        self.player1 = Player(card1, card2, 500)
    
    def testToString(self):
        self.assertEqual(self.player1.toString(),
            "Card1: 4H Card2: 6H Money:500 ")




if __name__ == "__main__":
    unittest.main()