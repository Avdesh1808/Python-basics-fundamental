#Execption Handling is the process of responding or unexpected events with a computer runs.
# it helps to skip and avoid the program or system crashing.
# without this system will disrupt the normal operation of a program.
# a=input("Enter a number : \n")
# print(f"multiplication of {a} is  :  ")
# try:
#     for i in range(1,11):
#         print(f"{int(a)}X{int(i)}={int(a)*i}")
# except Exception as e:
#     print(e)
# print("some inportant line of code")
# print("end fo the program")

try:
    num=int(input("Enter num in integer =  "))
except ValueError:
    print("no. entered is not an integer")