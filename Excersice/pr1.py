marks_str = input("enter your marks in under 100 : ")
marks_int = int(marks_str)
if marks_int >= 60 and marks_int <=100:
    print(f'your got {marks_int} passed and get 1st divison ')
elif marks_int >= 45 and marks_int <=100:
    print(f'your got {marks_int} passed and get 2nd divison ')
elif marks_int >= 33 and marks_int <=100:
    print(f'your  got {marks_int} passed and get 3rd divison ')
elif marks_int < 33 and marks_int <=100:
    print(print(f'your got {marks_int} you have failed better luck next time '))
else:
    print(print("You have entered undefined marks"))

# print name 5 times using while loop
i=0
while i<5:
    print("Avdesh")
    i+=1
# print list content using while loop
l=["P","Y","T","H","O","N"]
i=0
while (i<len(l)):
    print(l[i])
    i+=1
# print list content using for loop with else
l1=["P","Y","T","H","O","N"]
for i in l1:
    print(i)
else:
    print("done")

# for loop with break
for i in range(100):
    if(i==25):
        break   # exit the loop right now
    print(i)


# for loop with continue
for i in range(100):
    if(i==25):
        continue  # skip the iteration 
    print(i)

# print a table using for loop 
n = int(input("Enter a no.: "))
for i in range(1,11):
    print(f"{n}X{i}={n*i}")
    
l2=["Aman","Gopui","Avdesh","Ankur"]
for name in l2:
    if(name.startswith("A")):
        print(f"hello {name}")

# sum of natural no. using while loop

n=int(input("enter a no. "))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)



for letter in "Python":
    if letter == "h":
        continue
    print("Current Letter : ", letter) 


