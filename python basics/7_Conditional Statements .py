# Introduction to Control Flow
'''The if Statement 
The if statement is the most basic conditional construct. It executes a specific block 
of code only if a given condition evaluates to True.'''
# Basic if statement 
temperature = input("enter temperature ")
temperature_int = int(temperature)
if temperature_int >= 25:
    print(" its a warm day today ")
else:
    print("the day is normal ")


# if-else statement using age 
age_str = input("Enter your age :  ")
age_int = int(age_str)
if  age_int >=  18: 
    print(  "You are an adult."  )  # This block is skipped. 
else: 
    print(  "You are a minor."  )  # This block executes. 


# The if-elif-else Statement
# For scenarios involving multiple conditions, the if-elif-else structure is employed
# if-elif-else statement 
marks_str = input("Enter your marks which under and equals to the 100 : ")
marks_int = int(marks_str)
if marks_int >= 60:
    print(f"you have passed and got {marks_int} 1st division")
elif marks_int >= 45:
    print(f"you have passed and got {marks_int} 2nd division")
elif marks_int >= 33:
    print(f"you have passed and got {marks_int} 3nd division")
else:
    print(f"you have failed and got {marks_int} better luck nex time ")

# Nested if-else condition
weather = "sunny"
temperature1 = 28

if weather == "sunny":
    if temperature1 > 25:
        print("its hot and sunny day")
    else:
        print("its a pleasent sunny day")
else:
    print("its not sunny day")