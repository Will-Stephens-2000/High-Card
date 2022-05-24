import unittest
from card import *

class TestCardClass(unittest.TestCase):
    
    #def setUp(self):

         
    
    def testToString(self):
        nineH = Card("9", "H").toString()

        self.assertTrue(nineH, "9H")


if __name__ == "__main__":
    unittest.main()