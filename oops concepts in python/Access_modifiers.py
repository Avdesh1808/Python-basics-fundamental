# Access mofifiers/Specifiers
# used for limit tha access of class variables and class methods outside
class students:
    def __init__(self):
        self.__name = "Avdesh"# use (__) double underscore so that variable is become private and not accessable 
        self.__rollno = 12 # is want access so use 'name mangling' 
a=students()
print(a._students__name)# use this method for access private variable in class
print(a._students__rollno)
print(dir(a))