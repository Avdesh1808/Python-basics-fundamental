# create employee class in python
class Employee:
    def __init__(self,name):
        self.name=name

    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i
    def __str__(self):# str method used for print out an object
        return f"This employee's name is ('{self.name}') str "
    def __repr__(self):# while repr method used for get a string representation of an object
        return f"This employee's name is ('{self.name}') repr "
    def __call__(self):
        print(f"Hello my name is {self.name}")




