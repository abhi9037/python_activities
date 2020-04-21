import operator

mark_list = dict()
num = int(input("Enter number of students:"))
for i in range(1, num + 1):
    data = input("Enter %s'st student details:" % i)
    temp = data.split(':')
    mark_list[temp[0]] = int(temp[1])
print("Initial dictionary:\n", mark_list)
sorted_list = sorted(mark_list.items(), key=operator.itemgetter(1), reverse=False)
print("Sorted in ascending order:\n", sorted_list)


######################Sort by key#########################

for key in sorted(mark_list):
    print(key, mark_list[key])
