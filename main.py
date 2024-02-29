import keyword
import string

print(keyword.kwlist)
string_punctuation = string.punctuation + ' '

my_value = input('Enter name of value: ')
contains_letter = False

if my_value in keyword.kwlist:
    contains_letter = False
else:
    for i in my_value:
        if i in string.ascii_lowercase or i == '_':
            contains_letter = True
        if i in string.ascii_uppercase or my_value[0].isdigit() or i in string_punctuation and i != '_':
            contains_letter = False


if contains_letter:
    print(True)
else:
    print(False)



