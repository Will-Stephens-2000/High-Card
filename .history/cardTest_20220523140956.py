import unittest
from card import *

class TestCardClass(unittest.TestCase):
    
    def setUp(self):
        self.nineH = Card("9", "H")
         
    
    def testToString(self):
        #nineH = Card("9", "H").toString()

        self.assertTrue(self.nineH.toString(), "9H")


if __name__ == "__main__":
    unittest.main()