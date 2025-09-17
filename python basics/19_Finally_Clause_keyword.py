# It is also a part of exeption handling we can include a finally block at the end.
# finally works for exectuion your code at the end of programme where we want to execute of code after error
# Here is the example of code
def fun1():
    try:
        l=[1,2,3,6,4]
        i=int(input("Enter the index : "))# This code section used for throuing error use a latter in input
        print(l[i])
        return 0
    except:
        print("some error occured")# After throuhing are this ll show
        return 0
    
    finally:
        print("Code is always exected after throughing error")# finally this code will be executed weather error occured or not
    
x=fun1()
print(x)
