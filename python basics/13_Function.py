'''# This is the simple example of creating a function
def square(x):
    """This function is used for square of any natural no."""
    return x**2
x=int(input("Enter any no. for square = "))
out=square(x)
print(f"The square of {x} is = {out}")

def cube(y):
    """This function is used for cube of any natural no."""
    return y**3
y=int(input("Enter any no. for cube = "))
out=cube(y)
print(f"The cube of {y} is =  {out}")

# Positional Arguments  
def  nameAge  (name, age): 
 print(  f"Hi, I am  {name}  "  ) 
 print(  f"My age is  {age}  "  ) 
nameAge(  "Alice"  ,  30 )
print("1.This is positional arguments")

# Keyword Arguments 
def  student  (fname, lname): 
 print(fname, lname) 
student(lname=  'Practice'  , fname=  'Geeks'  )  # Order doesn't  matter with keywords.
print("2.This is keyword arguments and order doesn't matter with keywords")

# Default Arguments 
def f1(x,y=20):# we cant set predefined value in the function"s peramerters and after calling the function we can also overides the values of paramerters.
    print(f"X : {x}")
    print(f"Y : {y}")
print("3.This is Default arguments but also overides the values of parameters")
f1(100)
f1(10,30)

# Arbitrary Positional Arguments (*args)
def sum_all(*numbers):
   total = 0
   for num in numbers:
      total += num
   return total
print(f"Sum:  {sum_all(  1  ,  2  ,  3  ,  4  )}")
print(  f"Sum:  {sum_all(  10  ,  20  )}  "  )

# Arbitrary Keyword Arguments (**kwargs) [10] 
def  display_info  (**details):  # 'details' will be a  dictionary of all keyword arguments. 
 for  key, value  in  details.items(): 
  print(  f"  {key}  :  {value}  "  ) 
display_info(name=  "Alice"  , age=  30  , city=  "New York"  ) '''

#Function Scope
# LEGB Rule example
counter=0
global_var="I am Global" # global function
def outer_function():
  enclosing_var="I am enlosing var"
  def inner_function(): # nested defined functions
    #local_var = "I am local var"
    #print(local_var)
    #print(enclosing_var)  # Accesses enclosing  scope
    #print(global_var)  # Accesses global scope
    print(len('HELLO'))  # Accesses built-in scope
    





        






