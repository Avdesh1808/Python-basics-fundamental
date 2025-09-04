# This is the example of multiple inheritance
class student:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"{self.name} like dance.")
class dance:
    def __init__(self,name,dance):
        self.name=name
        self.dance_name=dance
    def show(self):
        print(f"{self.name} like dance.")
        print(f"{self.dance_name}")
class student_dance(student,dance):
    def show_dance(self):
        print("she like dance")
a = student_dance("Nikita")
a.show_dance()
a.show()


        
