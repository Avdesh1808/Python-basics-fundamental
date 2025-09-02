# The for Loop: Iterating over Sequences 
'''Loops, also known as iteration statements, are control flow constructs used to 
repeatedly execute a block of instructions until a specified condition is met.  7  They are 
essential for automating repetitive tasks and processing collections of data. '''
''' The for loop is designed to iterate over the items of any sequence (such as a list, 
tuple, string, or range) or other iterable objects'''
# Iterating over a list 
words = ("one","two","three","four","five","six")
for  i  in  words:  # 'x' takes on each value in 'words' sequentially.
    print(i)

# Iterating over a string
word = "PYTHON"
for char in word:
    print(char)

# Using range() for numerical iteration 
for  num  in  range  (2):  # Generates numbers from 0 up to  (but not including) 5.
    print(num)


 # The while Loop: Conditional Iteration
'''The while loop continuously executes a block of code as long as a given Boolean 
condition remains True.  7  The loop continues to iterate  until the condition evaluates to 
False.''' 


# Basic while loop
n = 1
while n < 6:   # Loop continues as long as 'i' is less  than 6.
    print(n)  # Increment 'i' to eventually make the  condition False.
    n += 1


# break and continue Statements 
'''Jump statements, such as break and continue, allow for alteration of the normal flow 
within a loop.  7 
●  The break statement immediately terminates the current loop entirely, transferring 
program control to the statement directly following the loop. 
●  The continue statement skips the remainder of the current iteration within the 
loop and proceeds to the beginning of the next iteration.'''


x = 0
while x<10:
    print("x:",x)
    if x==5:
        print("breaking...")
        break
    x+=1
print("end")

# Using continue [7] 
for  letter  in  "Python"  : 
    if  letter ==  "h"  :  # Skips printing 'h' and continues  to the next letter. 
        continue 
    print(  "Current Letter :"  , letter) 
# Output: Current Letter : P, Current Letter : y, Current Letter : t, Current Letter : o, Current Letter : n 

# Nested Loops 
'''Nested loops involve placing one loop inside another. The inner loop executes 
completely for each iteration of the outer loop.'''

# Nested for loops 
for  i  in  range  (  3  ):  # Outer loop iterates 3 times. 
    for  j  in  range  (  2  ):  # Inner loop iterates 2 times  for each outer iteration. 
        print(  f"(  {i}  ,  {j}  )"  ) 
# Output: (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)