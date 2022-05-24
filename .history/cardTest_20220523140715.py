import unittest
from card import *

class TestCardClass(unittest.TestCase):
    
    #def setUp(self):

         
    
    def testToString(self):
        nineH = Card("9", "H")
        self.assertTrue(nineH.toString(), "9H")


if __name__ == "__main__":
    unittest.main()