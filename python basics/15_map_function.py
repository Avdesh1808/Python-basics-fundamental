# MAP() This is the example of map the function
def cube(x):
    return x*x*x
#print(cube(2))
l=[2,3,6,5,4,8,6,7] 
newl=list(map(cube,l))
print(newl)