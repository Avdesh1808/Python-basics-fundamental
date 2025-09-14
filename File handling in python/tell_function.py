# tell() function used for finda a position of bytes in file
with open('File handling in python/T.txt','r') as f:
    f.seek(13)# used to skip 13 bytes or letter in a file
    print(f"That is the position of bytes where start to read bytes : {f.tell()}th position")# it will tell a right position of byte where bytes ll start to read in file
    data=f.read(5)#Read next 5 bytes or letter in a file
