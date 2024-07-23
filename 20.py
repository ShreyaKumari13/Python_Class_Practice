'''
    20. Write a Python class to reverse a string word by word.
    Input string : 'hello .py'
    Expected Output : '.py hello'
'''
# class Reverse:
#     def reverse_words(self, s):
#         return ' '.join(reversed(s.split()))
# print(Reverse().reverse_words('hello'))

class Reverse:
    def reverse_words(self, s):
        a = list(reversed(s))
        return "".join(a)
print(Reverse().reverse_words('hello'))

