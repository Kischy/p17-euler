# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:33:08 2019

@author: kisch
"""

class NumberToWords():   
    
    __N_to_W__ = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", \
                    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", \
                    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", \
                    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", \
                    19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", \
                    50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", \
                    90: "ninety", 100: "hundred", 1000: "thousand"}
    
    
    def __get_thousands__(self,number): 
        how_many = number // 1000
        
        if(how_many > 0):
            return NumberToWords.__N_to_W__[how_many] + NumberToWords.__N_to_W__[1000]
        
        return ""
    

    def __get_hundreds__(self,number):
        how_many = number // 100
        
        if(how_many > 0):
            return NumberToWords.__N_to_W__[how_many] + NumberToWords.__N_to_W__[100]
                   
        return ""
    
    
    
    def __get_result_til_tens__(self,number):
        res_til_tens = self.__get_thousands__(number)
        number = number % 1000
        
        res_til_tens += self.__get_hundreds__(number)  
        
        return res_til_tens
    
    

    def __get_tens__(self,number):
        
        first_digit_relevant = False
        
        if(number >= 10 and number <= 19  ):
             return NumberToWords.__N_to_W__[number], first_digit_relevant
        elif(number >= 20 and number <= 99):
             tens = number // 10
             first_digit_relevant = True
             return NumberToWords.__N_to_W__[tens*10], first_digit_relevant
                   
        return "", True
    
    

    def __get_single_digit__(self,number):
        
        if(number > 0):
            return NumberToWords.__N_to_W__[number]
                   
        return ""    

    
    
    def __get_result_from_tens__(self,number):
        ten_res, first_digit_relevant = self.__get_tens__(number)       
        res_from_tens = ten_res 
        
        if(first_digit_relevant):
            number = number % 10
            res_from_tens += self.__get_single_digit__(number) 

        return res_from_tens
    
    def __concatenate_results__(self, res_til_tens, res_from_tens):
        
        if( res_from_tens != "" and res_til_tens != ""):
            return res_til_tens + "and" + res_from_tens
        else:
            return res_til_tens + res_from_tens
        
    
                
    def make_word(self,number):      
        res_til_tens = self.__get_result_til_tens__(number)
        number = number % 100       

        res_from_tens = self.__get_result_from_tens__(number)
            
        result = self.__concatenate_results__(res_til_tens, res_from_tens)      

        
        return result


