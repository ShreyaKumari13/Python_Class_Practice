'''
    14. Write a Python class to convert a roman numeral to an integer.
'''
class Convert:
    def roman_to_int(self,roman):
        roman_num = {"I":1,"V":5,"X":10,"L":50,"C":100}
        int_val = 0
        for i in range(len(roman)):
            if i > 0 and roman_num[roman[i]] > roman_num[roman[i - 1]]:
                int_val += roman_num[roman[i]] - 2 * roman_num[roman[i - 1]]
            else:
                int_val += roman_num[roman[i]]
        return int_val

print(Convert().roman_to_int('X'))
print(Convert().roman_to_int('C'))


# class Convert:
#     def roman_to_int(self, s):
#         rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
#         int_val = 0
#         for i in range(len(s)):
#             if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
#                 int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
#             else:
#                 int_val += rom_val[s[i]]
#         return int_val

# print(Convert().roman_to_int('C'))