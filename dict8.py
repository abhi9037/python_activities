from collections import defaultdict, Counter
str1 = input("Enter a string : ")
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)