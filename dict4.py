val1 = list()
val2 = list()
data1 = input("Enter list 1: ")
data2 = input("Enter list 2: ")
data1 = data1.split()
data2 = data2.split()
dict1 = dict(zip(data1,data2))
print(dict1)