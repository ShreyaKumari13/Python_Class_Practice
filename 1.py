'''
    1. Write a Python program to import built-in array module and display the namespace of the said module.
'''
import array
for i in array.__dict__:
    print(i)