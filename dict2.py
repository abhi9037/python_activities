d1 = {'a':10,'b':12}
d2 = {'c':14,'d':15}
d3 = {'e':30,'e':20,'e':15}
dict = {}
for i in (d1,d2,d3):
    print(i)
    dict.update(i)
print(dict)