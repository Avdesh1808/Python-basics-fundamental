# swapping two numbers in python (1) for save time 
x = 10
y = 15
x , y = y , x
print("After swapping 10 in x = ",x)
print("After swapping 15 in y = ",y)

# (2) normal using temp
temp = x # store a value in x for temprory using temp 
x = y # swapping temprory vlaue in y
y = temp # set y to the original value
print("After swapping 10 in x = ",x)
print("After swapping 15 in y = ",y)
