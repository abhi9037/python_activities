# convert a list into a nested dictionary of keys.

new_dict = current = {}
new_list = [1, 2, 3, 4, 5]
for num in new_list:
    current[num]= {}
    current = current[num]
print(current)
print(new_dict)