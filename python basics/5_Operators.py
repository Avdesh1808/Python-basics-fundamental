# Arithmetic Operators 
a =  10 
b =  3 
print(  f"Addition (a + b):  {a + b}  "  )  
# Output:  13 
print(  f"Subtraction (a - b):  {a - b}  "  )  # Output:  7 
print(  f"Multiplication (a * b):  {a * b}  "  )  # Output:  30 
print(  f"Division (a / b):  {a / b}  "  )  
# Output:  3.333... (float division) 
print(  f"Floor Division (a // b):  {a // b}  "  )  # Output:  3 (integer division) 
print(  f"Modulus (a % b):  {a % b}  "  )  
# Output:  1 (remainder) 
print(  f"Exponentiation (a ** b):  {a ** b}  "  )  # Output:  1000 (10 to the power of 3)
c=2
d=3
print(f"Exponentiation 2 ** 3: {c**d} ")

# Comparison Operators 
x =  5 
y =  10 
print(  f"x == y:  {x == y}  "  )  # Output: False (equal  to) 
print(  f"x!= y:  {x!= y}  "  )  # Output: True (not equal  to) 
print(  f"x > y:  {x > y}  "  )  # Output: False (greater  than) 
print(  f"x < y:  {x < y}  "  )  # Output: True (less than) 
print(  f"x >= 5:  {x >=  5  }  "  )  # Output: True (greater  than or equal to) 
print(  f"y <= 10:  {y <=  10  }  "  )  # Output: True (less than  or equal to) 

# Logical Operators 
is_sunny =  True 
is_warm =  False 
print(  f"is_sunny and is_warm:  {is_sunny  and  is_warm}  "  )  # Output: False (both True) 
print(  f"is_sunny or is_warm:  {is_sunny  or  is_warm}  "  )  # Output: True (at least one True) 
print(  f"not is_sunny:  {  not  is_sunny}  "  )  





# Assignment Operators 
total =  10 
total +=  5  # Equivalent to: total = total + 5 
print(  f"total after += 5:  {total}  "  )  # Output: 15 
total -=  3  # Equivalent to: total = total - 3 
print(  f"total after -= 3:  {total}  "  )  # Output: 12 
product =  5 
product *=  2  # Equivalent to: product = product *  2 
print(  f"product after *= 2:  {product}  "  )  # Output:  10


# Identity Operators 
''' These operators (is, is not) compare the memory locations (identities) of two objects, 
determining if they refer to the exact same object in memory. 
Python'''
list1 = 1
list2 = 2
list3 = list1 
print(  f"list1 is list2:  {list1  is  list2}  "  )  # Output:  False (different memory locations) 
print(  f"list1 is list3:  {list1  is  list3}  "  )  # Output:  True (refer to the same object) 
print(  f"list1 is not list2:  {list1  is  not  list2}  "  )  # Output: True


# Membership Operators
'''These operators (in, not in) test whether a value is present within a sequence (such as 
a string, list, tuple, or set). 
Python ''' 
my_string =  "Python"
print(  f"'P' in my_string:  {  'P'  in  my_string}  "  )  
# Output: True

# Operator Precedence Example 
result =  2  +  3  *  4  # Multiplication (3 * 4 = 12)  happens before addition (2 + 12 = 14) 
print(  f"2 + 3 * 4 =  {result}  "  )  # Output: 14 
result_with_parentheses = (  2  +  3  ) *  4  # Parentheses  override: (2 + 3 = 5) then (5 * 4 = 20) 
print(  f"(2 + 3) * 4 =  {result_with_parentheses}  "  )  # Output: 20