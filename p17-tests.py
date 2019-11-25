# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:33:08 2019

@author: kisch
"""


import unittest

from NumberToWords import NumberToWords


class TestCollatzLength(unittest.TestCase):
    
    def setUp(self):
        self.N_to_W = NumberToWords()
    
    def test_make_words(self):
        self.assertEqual(self.N_to_W.make_word(1),"one")
        self.assertEqual(self.N_to_W.make_word(2),"two")
        self.assertEqual(self.N_to_W.make_word(3),"three")
        self.assertEqual(self.N_to_W.make_word(4),"four")
        self.assertEqual(self.N_to_W.make_word(5),"five")
        self.assertEqual(self.N_to_W.make_word(6),"six")
        self.assertEqual(self.N_to_W.make_word(7),"seven")
        self.assertEqual(self.N_to_W.make_word(8),"eight")
        self.assertEqual(self.N_to_W.make_word(9),"nine")
        self.assertEqual(self.N_to_W.make_word(10),"ten")
        self.assertEqual(self.N_to_W.make_word(11),"eleven")
        self.assertEqual(self.N_to_W.make_word(12),"twelve")
        self.assertEqual(self.N_to_W.make_word(342 ),"threehundredandfortytwo")
        self.assertEqual(self.N_to_W.make_word(300 ),"threehundred")
        self.assertEqual(self.N_to_W.make_word(301 ),"threehundredandone")
        self.assertEqual(self.N_to_W.make_word(511 ),"fivehundredandeleven")
        self.assertEqual(self.N_to_W.make_word(983),"ninehundredandeightythree")
        self.assertEqual(self.N_to_W.make_word(1000),"onethousand")




if __name__ == '__main__':
    unittest.main(verbosity=0)
