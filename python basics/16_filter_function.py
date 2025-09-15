# Filter() function use for finad a particular value from the data
l=[2,3,6,5,4,8,3,2,4,6,5]
def function(a):
    return a>2
newl=list(filter(function,l))# In the output we'll se that number wwhich is greater than 2
print(newl)