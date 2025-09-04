# This is the example of Multilevel inheritance
class Grandparent:
    def grandparent_function(self,name):
        self.name=name
        print(f"Hi i am grandparent '{self.name}'")
class Parent(Grandparent):
    def parent_function(self,name):
        self.name=name
        print(f"Hi i am parent drived from grandparent '{self.name}'")
class Child(Parent):
    def child_function(self,name):
        self.name=name
        print(f"Hi i am child drived from parent '{self.name}'")
a=Child()
a.grandparent_function("Grand Father")
a.parent_function("Father")
a.child_function("Son")


