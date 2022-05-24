import unittest
from card import *

class TestCardClass(unittest.TestCase):
    nineH = Card("9", "H")
    #def setUp(self):

         
    
    def testToString(self):
        self.assertTrue(nineH.toString(), "9H")


if __name__ == "__main__":
    unittest.main()