# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:33:08 2019

@author: kisch
"""

class NumberToWords():   
    
    numsToWords = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", \
                    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", \
                    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", \
                    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", \
                    19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", \
                    50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", \
                    90: "ninety", 100: "hundred", 1000: "thousand"}
    
    
    def get_thousands(self,number): 
        thous = number // 1000
        
        if(thous > 0):
            return NumberToWords.numsToWords[thous] + NumberToWords.numsToWords[1000]
        
        return ""

    def get_hundreds(self,number):
        hun = number // 100
        
        if(hun > 0):
            return NumberToWords.numsToWords[hun] + NumberToWords.numsToWords[100]
                   
        return ""

    def get_tens(self,number):
        
        first_digit_relevant = False
        
        if(number >= 10 and number <= 19  ):
             return NumberToWords.numsToWords[number], first_digit_relevant
        elif(number >= 20 and number <= 99):
             tens = number // 10
             first_digit_relevant = True
             return NumberToWords.numsToWords[tens*10], first_digit_relevant
                   
        return "", True

    def get_single_digit(self,number):
        
        if(number > 0):
            return NumberToWords.numsToWords[number]
                   
        return ""
    
    def get_result_til_tens(self,number):
        res_til_tens = self.get_thousands(number)
        number = number % 1000
        
        res_til_tens += self.get_hundreds(number)  
        
        return res_til_tens
    
    
    def get_result_from_tens(self,number):
        ten_res, first_digit_relevant = self.get_tens(number)       
        res_from_tens = ten_res 
        
        if(first_digit_relevant):
            number = number % 10
            res_from_tens += self.get_single_digit(number) 

        return res_from_tens
    
    def concencate_results(self, res_til_tens, res_from_tens):
        
        if( res_from_tens != "" and res_til_tens != ""):
            return res_til_tens + "and" + res_from_tens
        else:
            return res_til_tens + res_from_tens
        
    
                
    def make_word(self,number):      
        res_til_tens = self.get_result_til_tens(number)
        number = number % 1000
        number = number % 100       

        res_from_tens = self.get_result_from_tens(number)
            
        result = self.concencate_results(res_til_tens, res_from_tens)      

        
        return result


