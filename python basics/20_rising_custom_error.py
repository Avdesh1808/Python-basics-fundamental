# for exception handling we ll use raise value error:
a=int(input("Enter any Value between 5 and 9  : \n"))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")
else:
    print("pass and execute code")