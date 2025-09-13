# READING A FILE
# This code is use for how to hadle the files.use to perform different operation on file    
# f=open("T.txt","r")# "r" used to read a file and it is also by default
# text=f.x()

# WRITING TO A FILE
# f=open("T.txt","w")# "w" used to write in file 
# text=f.write("Hello this is a Avdesh Chauhan")
# print(text)

# APPEND TO A FILE 
#f=open("T.txt","a")
#text=f.write(" Hello this is Yash")
#print(text)
#f.close()

# SECOND WAY TO WRTIE A CODE USING 'with'
with open("T.txt",'a') as f:
    f.write(" Hello this is Aman ") # and it is automatically close

    

