class myclass:
    def __init__(self,value):
        self.value = value
    def show(self):
        print(f"Value is {self.value}")
    @property
    def ten_multiple(self):
        return 10*self.value
    @ten_multiple.setter
    def ten_multiple(self,new_value):
        self.value = new_value/10
obj=myclass(30)
obj.ten_multiple = 200
print(obj.ten_multiple) 
obj.show()