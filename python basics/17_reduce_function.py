# this is the code example of reduce function when we have to add the numbers through this function
from functools import reduce 
numbers=[2,3,6,4,5,7,9,4,6,]
# now calculate the sum  of numbers using reduce function
sum=(reduce(lambda x,y:x+y,numbers))# there is not need to type cast here into list
print(sum)