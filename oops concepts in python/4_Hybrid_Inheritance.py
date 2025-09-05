# This is the example of Hybrid inhertance
"""
            grand class
        _________|__________
        |                  |
    parent class        parent.1 class
        |________ _________|
                | |
            child class

"""
class grand:
    def grand_fun(self,name):
        self.grand_name=name
        print(f"I am grand function '{name}'")
class parent(grand):
    def parent_fun(self,name):
        self.parent_name=name
        print(f"I am parent function '{name}'")
class parent1(grand):
    def parent1_fun(self,name):
        self.parent1_name=name
        print(f"I am parent.1 function '{name}'")
class child(parent,parent1):
    def child_fun(self,name):
        self.child_name=name
        print(f"I am child function '{name}'")
a=child()
a.child_fun("Avdesh")
a.parent1_fun("Mother")
a.parent_fun("Father")
a.grand_fun("Grand Father")