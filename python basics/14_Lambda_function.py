# lambda fuction is often to use where small function is required in a one line
# Here is the example of Lambda function
square=lambda x:x*x # This function is often to write in a single line
print(square(2))
cube=lambda x:x*x*x
print(cube(2))
# we can also use a function as  a parameters in a other function
def other(fx,value):
    return 6+fx(value)
print(other(square,2))
