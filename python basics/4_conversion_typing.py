 # Type conversion examples 
'''Type conversion involves changing data from one type to another using built-in functions like int(), float(), str(), and bool().'''
num_str = '123'
num_int = int(num_str) # convert string into integer
print(type(num_int))

# conversion float value into integer
float_value = 11.66
int_value = int(float_value)
print(type(int_value))

# now add both integer
print(num_int+int_value)

# conversion int into string
int_value = 11.66
str_value = str(int_value)
print(type(str_value))