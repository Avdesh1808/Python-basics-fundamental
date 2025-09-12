# This is a part of polymorphism
# That is the code example of Method overlaoding
# Where method are same name but no. of parameters can be more and different
class addition:
    def add(*nums):
        return sum(nums)
a=addition
print(a.add(1,3,5))# Here method is same add() but perameters are different
print(a.add(3,6,5,9,8))
print(a.add(30,20,50,60))