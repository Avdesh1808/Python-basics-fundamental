# truncate() fucntion used for create a specific size of bytes in a file
# It work in 'w' 'a' file mode
with open("File handling in python/T.txt","w") as f:
    f.write("Hello world")
    f.truncate(6)
with open("File handling in python/T.txt","r") as f:
    print(f.read())
