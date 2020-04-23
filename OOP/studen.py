
class Student():
    student_list = []
    def createStudent(self):
        name = input("Enter the name of student: ")
        marks = input("Enter the marks: ")
        mark = marks.split(',')
        mark_list = [int(m) for m in mark]
        data = {
            'name':name,
            'mark':mark_list
        }
        self.student_list.append(data)
        return data

    def average_mark(self,student):
        if student['mark'] :
            return sum(student['mark'])/len(student['mark'])
        else:
            print("No marks are available")

    def student_details(self,student):
        print("{}, Average mark: {}".format(student['name'],self.average_mark(student)))

    def print_student_details(self,students):
        if students:
            for student in students:
                self.student_details(student)
        else:
            print("Student list is empty !!!!")

    def menu(self):
        selection = input("Select an option:\n"
                          "A: Create student\n"
                          "B: Print Student list\n"
                          "Q: Quit\n")
        while selection != 'Q':
            if selection == 'A' or selection == 'a':
                self.createStudent()
                self.menu()
            elif selection == 'B' or selection == 'b':
                self.print_student_details(self.student_list)
                self.menu()
            else:
                print("Wrong choice!!!!!")
                break
        exit()


obj = Student()
obj.menu()
