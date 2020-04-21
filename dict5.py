from heapq import nsmallest
num = int(input("Enter number of students:"))
mark_list = {}
for i in range(1, num + 1):
    data = input("Enter %s'st student details:" % i)
    temp = data.split(':')
    mark_list[temp[0]] = int(temp[1])
three_largest = nsmallest(3,mark_list, key=mark_list.get)
print(three_largest)