print("-:welcome to calculator:-")
a = int(input("enter your 1st no : "))
user_ip1 = str(input("enter +,-,/,* : "))
b = int(input("enter your 3rd no : "))

if user_ip1 == '+':
    print(a+b)
    print(f"Here is your result  : {a+b}")
elif user_ip1 == '-':
    print(a-b)
    print(f"Here is your result  :{a-b}")
elif user_ip1 == '*':
    print(a*b)
    print(f"Here is your result  : {a*b}")
elif user_ip1 == '/':
    print(a/b)
    print(f"Here is your result  :{a/b}")
else:
    pass
