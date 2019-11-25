# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:16:13 2019

@author: kisch
"""

from NumberToWords import NumberToWords


problem_number = 17


print("Calculation started")


NToWords = NumberToWords()


the_answer = 0

for i in range(1,1001):
    the_answer += len(NToWords.make_word(i))




print("The answer to the " + str(problem_number) + "th problem of ProjectEuler.Net is:",the_answer)
