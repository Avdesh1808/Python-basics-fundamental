# super keyword use for overide a function which is used by inherit class which is derived from base class
# Here is the code example of super() keyword
class employee:
    def __init__(self,name,id):
        self.employee_name=name
        self.employee_id=id
        print(f"{self.employee_name} {self.employee_id}")
class programmer(employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)# Here super() keyword used for overide functions from base class 'employee' the will be use in derived class
        self.programmer_lang=lang
        print(f"Name = {name}, id = {id}, lang = {lang}")
a=programmer("Avdesh","231","Python")
