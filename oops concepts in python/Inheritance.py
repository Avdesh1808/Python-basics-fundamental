# THIS IS THE CODE EXAMPLE OF INHERITANCE
class students:
    def __init__(self,name,roll_no):
        self.student_name = name
        self.student_roll_no = roll_no
    
    def students_details(self):
        print(f"{self.student_name},{self.student_roll_no}")
class employee(students): # this is a part of new derived class from old class.
    def showid(self):
        print("This is employee object")
a=students('Avdesh',16)
a.students_details()
b=employee('Pooja',2316)
b.students_details()
b.showid()