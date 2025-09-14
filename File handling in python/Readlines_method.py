# Example of realine and manage the data in txt file 
f=open('File handling in python/T.txt','r')# define the loaction of directry of file, where file created
i=0 # i is a line of a rows students
while True:
    i+=1
    line=f.readline()
    if not line:
        break
    m1=int(line.split(" ")[0])
    m2=int(line.split(" ")[1])
    m3=int(line.split(" ")[2])
    print(f"Marks of Student {i} in math is {m1}")# print student column subject 1
    print(f"Marks of Student {i} in english is {m2}")# print student column subject 2
    print(f"Marks of Student {i} in SST is {m3}")# print student column subject 3
    print("\n ")

        

        