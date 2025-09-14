#seek() function used for skip bytes in file.
with open('File handling in python/T.txt','r') as f:
    f.seek(10)# it will skip 10 letter then print left data
#Read only 5 letter  
    data=f.read(5)
    print(data)