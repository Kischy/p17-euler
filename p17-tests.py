# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:33:08 2019

@author: kisch
"""


import unittest

from NumberToWords import NumberToWords as NtoW


class TestCollatzLength(unittest.TestCase):
    
    def setUp(self):
        self.N_to_W = NtoW()
    
    def test_number_to_words(self):
        self.assertEqual(self.N_to_W(1),"one")
        self.assertEqual(self.N_to_W(2),"two")
        self.assertEqual(self.N_to_W(3),"three")
        self.assertEqual(self.N_to_W(4),"four")
        self.assertEqual(self.N_to_W(5),"five")
        self.assertEqual(self.N_to_W(6),"six")
        self.assertEqual(self.N_to_W(7),"seven")
        self.assertEqual(self.N_to_W(8),"eight")
        self.assertEqual(self.N_to_W(9),"nine")
        self.assertEqual(self.N_to_W(10),"ten")
        self.assertEqual(self.N_to_W(11),"eleven")
        self.assertEqual(self.N_to_W(12),"twelve")
        self.assertEqual(self.N_to_W(342 ),"threehundredandfortytwo)")
        #Add more testcases 




if __name__ == '__main__':
    unittest.main(verbosity=0)
