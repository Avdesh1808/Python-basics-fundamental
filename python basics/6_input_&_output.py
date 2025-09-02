# use some built in function in python , print() function
# printing simple string
print("hello world !") # Display the string literal.

# printing messege on console
message = "learning is fun"
print(message)

name = 'Avdesh'
age = 22
print("name : ",name,"\nage : ",age)

# use input() function to take input from user on console
# Getting simple string input 
user_name =  input  (  "Please enter your name: "  )  # Prompts  user and stores input as string. 
print(  f"Hello,  {user_name}  !"  )  # Uses an f-string for  formatted output. 


# Input with type conversion 
age_str = input("Enter your age : ")
age_int = int(age_str)
print(f"In upcoming next year you will be {age_int+1} years old")