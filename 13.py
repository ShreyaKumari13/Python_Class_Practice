'''
    13. Write a Python class to convert an integer to a roman numeral.
'''
class Convert:
    def int_to_roman(self,num):
        roman_num = ""
        val = [10, 9, 5, 4,1]
        syb = ["X", "IX", "V", "IV","I" ]
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
print(Convert().int_to_roman(5))
print(Convert().int_to_roman(10))
print(Convert().int_to_roman(9))
print(Convert().int_to_roman(4))
print(Convert().int_to_roman(10))

class Convert:
    def int_to_roman(num):
        roman_num = ""
        val = [10, 9, 5, 4,1]
        syb = ["X", "IX", "V", "IV","I" ]
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
print(Convert.int_to_roman(5))





    
 
   
            

  


